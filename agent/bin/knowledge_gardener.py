#!/usr/bin/env python3
"""
D4rk Mind — Knowledge Gardener Agent
A persistent agent that continuously grows MemPalace with deep domain expertise.

Sources it studies:
- Component libraries (Radix, shadcn/ui, Chakra, etc.)
- Design system documentation
- API specifications
- Security patterns
- Algorithm implementations
- Architecture patterns

Usage:
    python knowledge_gardener.py              # Run once
    python knowledge_gardener.py --daemon    # Run forever
    python knowledge_gardener.py --sources   # List available sources
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

try:
    import chromadb
    import httpx
    CHROMA_AVAILABLE = True
except ImportError:
    CHROMA_AVAILABLE = False


PALACE_PATH = str(Path.home() / ".mempalace" / "palace")

# Knowledge sources configuration
class Wing(Enum):
    FRONTEND = "expert-frontend"
    BACKEND = "expert-backend"
    AUTH = "expert-auth"
    SECURITY = "expert-security"
    OPTIMIZATION = "expert-optimization"
    ORCHESTRATION = "expert-orchestration"
    DESIGN_SYSTEMS = "design-systems"
    COMPONENTS = "components"
    ARCHITECTURE = "architecture"


@dataclass
class KnowledgeSource:
    """A source of knowledge to mine."""
    name: str
    url: str
    wing: Wing
    room: str
    description: str
    patterns: List[str]  # Search patterns to extract
    last_mined: Optional[str] = None
    frequency_hours: int = 24


class KnowledgeGardener:
    """Agent that continuously grows MemPalace with deep knowledge."""
    
    # Pre-configured knowledge sources
    SOURCES: List[KnowledgeSource] = [
        # Frontend Components
        KnowledgeSource(
            name="Radix UI Primitives",
            url="https://raw.githubusercontent.com/radix-ui/primitives/main/packages/react/src/components",
            wing=Wing.FRONTEND,
            room="components/radix",
            description="Headless UI primitives for React - accessible, unstyled components",
            patterns=["accordion", "alert-dialog", "aspect-ratio", "avatar", "checkbox", "collapsible", 
                     "context-menu", "dialog", "dropdown-menu", "hover-card", "label", "navigation-menu",
                     "popover", "progress", "radio-group", "scroll-area", "select", "separator",
                     "slider", "switch", "tabs", "toggle", "toggle-group", "tooltip"],
        ),
        KnowledgeSource(
            name="shadcn/ui Components",
            url="https://raw.githubusercontent.com/shadcn-ui/ui/main/apps/www/content/docs/components",
            wing=Wing.FRONTEND,
            room="components/shadcn",
            description="Beautifully designed components built with Radix UI and Tailwind CSS",
            patterns=["accordion", "alert", "aspect-ratio", "avatar", "badge", "button", "calendar",
                     "card", "carousel", "checkbox", "collapsible", "command", "context-menu",
                     "data-table", "date-picker", "dialog", "dropdown-menu", "form", "hover-card",
                     "input", "label", "menubar", "navigation-menu", "pagination", "popover", "progress",
                     "radio-group", "select", "separator", "sheet", "skeleton", "slider", "sonner",
                     "switch", "table", "tabs", "textarea", "toast", "toggle", "toggle-group", "tooltip"],
        ),
        KnowledgeSource(
            name="Headless UI",
            url="https://headlessui.com/react",
            wing=Wing.FRONTEND,
            room="components/headlessui",
            description="Completely unstyled, accessible UI components",
            patterns=["menu", "listbox", "combobox", "dialog", "disclosure", "radio-group", 
                     "switch", "tabs", "transition"],
        ),
        KnowledgeSource(
            name="Chakra UI Components",
            url="https://chakra-ui.com/docs/components",
            wing=Wing.FRONTEND,
            room="components/chakra",
            description="Simple, modular and accessible component library",
            patterns=["alert", "avatar", "badge", "button", "card", "checkbox", "close-button",
                     "code", "container", "divider", "drawer", "form-control", "heading", "icon",
                     "image", "input", "kbd", "link", "list", "menu", "modal", "number-input",
                     "progress", "radio", "select", "skeleton", "skip-nav", "spinner", "stat",
                     "switch", "table", "tabs", "tag", "textarea", "tooltip"],
        ),
        
        # Design Systems
        KnowledgeSource(
            name="Tailwind CSS Components",
            url="https://tailwindcss.com/docs",
            wing=Wing.DESIGN_SYSTEMS,
            room="tailwind",
            description="Utility-first CSS framework patterns",
            patterns=["flexbox", "grid", "spacing", "typography", "colors", "border", "shadow",
                     "animation", "transition", "transform", "layout", "positioning", "responsive",
                     "dark-mode", "container", "columns", "aspect-ratio", "isolation"],
        ),
        KnowledgeSource(
            name="Radix Colors",
            url="https://www.radix-ui.com/colors",
            wing=Wing.DESIGN_SYSTEMS,
            room="colors/radix",
            description="Accessible color palette system",
            patterns=["gray", "mauve", "slate", "sage", "olive", "sand", "amber", "orange",
                     "tomato", "red", "ruby", "crimson", "pink", "plum", "purple", "violet",
                     "iris", "indigo", "blue", "cyan", "teal", "jade", "green", "grass",
                     "lime", "yellow", "amber"],
        ),
        KnowledgeSource(
            name="IBM Carbon Design",
            url="https://carbondesignsystem.com/components",
            wing=Wing.DESIGN_SYSTEMS,
            room="carbon",
            description="IBM's design system for products and experiences",
            patterns=["button", "accordion", "breadcrumb", "checkbox", "code-snippet", "combo-box",
                     "content-switcher", "data-table", "date-picker", "dropdown", "file-uploader",
                     "footer", "header", "inline-loading", "link", "list", "loading", "modal",
                     "notification", "number-input", "overflow-menu", "pagination", "progress-bar",
                     "radio-button", "search", "select", "side-nav", "slider", "structured-list",
                     "tabs", "tag", "text-input", "tile", "toggle", "tooltip", "tree-view"],
        ),
        
        # Accessibility Patterns
        KnowledgeSource(
            name="ARIA Authoring Practices",
            url="https://www.w3.org/WAI/ARIA/apg/patterns",
            wing=Wing.FRONTEND,
            room="accessibility/aria-patterns",
            description="W3C ARIA Authoring Practices Guide patterns",
            patterns=["accordion", "alert", "breadcrumbs", "button", "checkbox", "combobox",
                     "dialog", "disclosure", "feed", "landmarks", "link", "listbox", "menu",
                     "menu-button", "radio-group", "scrollable-box", "search", "slider",
                     "spinbutton", "switch", "table", "tabs", "treeview", "widget"],
        ),
        
        # Animation Libraries
        KnowledgeSource(
            name="Framer Motion",
            url="https://www.framer.com/motion",
            wing=Wing.FRONTEND,
            room="animation/framer",
            description="Production-ready motion library for React",
            patterns=["animation", "transition", "gesture", "layout", "scroll", "exit", "enter",
                     "variants", "keyframes", "spring", "tween", "drag", "pan", "hover", "tap",
                     "focus", "while-in-view", "use-animation", "use-scroll", "AnimatePresence"],
        ),
        KnowledgeSource(
            name="GSAP",
            url="https://greensock.com/docs",
            wing=Wing.FRONTEND,
            room="animation/gsap",
            description="Professional-grade animation library",
            patterns=["tween", "timeline", "gsap.to", "gsap.from", "gsap.fromTo", "stagger",
                     "ScrollTrigger", "ScrollSmoother", "SplitText", "MotionPathPlugin",
                     "Draggable", "EaselPlugin", "TextPlugin", "DrawSVGPlugin", "MorphSVGPlugin"],
        ),
        
        # Backend Patterns
        KnowledgeSource(
            name="Node.js Best Practices",
            url="https://github.com/goldbergyoni/nodebestpractices",
            wing=Wing.BACKEND,
            room="nodejs",
            description="Big Node.js Security Best Practices",
            patterns=["security", "structuring", "dependencies", "error-handling", "api",
                     "databases", "testing", "ci-cd", "production", "docker", "graphql"],
        ),
        KnowledgeSource(
            name="REST API Design",
            url="https://restfulapi.net",
            wing=Wing.BACKEND,
            room="api/rest",
            description="REST API design best practices",
            patterns=["resource-naming", "http-methods", "status-codes", "pagination",
                     "filtering", "versioning", "authentication", "error-handling", "caching",
                     "content-negotiation", "hypermedia", "rate-limiting"],
        ),
        KnowledgeSource(
            name="GraphQL",
            url="https://graphql.org",
            wing=Wing.BACKEND,
            room="api/graphql",
            description="GraphQL query language patterns",
            patterns=["query", "mutation", "subscription", "schema", "type", "input", "enum",
                     "interface", "union", "directive", "variable", "fragment", "alias"],
        ),
        
        # Security
        KnowledgeSource(
            name="OWASP Top 10",
            url="https://owasp.org/Top10",
            wing=Wing.SECURITY,
            room="owasp",
            description="Most critical security risks to web applications",
            patterns=["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10",
                     "broken-access", "cryptographic", "injection", "insecure-design", 
                     "security-misconfig", "vulnerable-components", "auth-failures",
                     "software-integrity", "logging-failures", "ssrf"],
        ),
        KnowledgeSource(
            name="Security Headers",
            url="https://securityheaders.com",
            wing=Wing.SECURITY,
            room="headers",
            description="HTTP security headers guide",
            patterns=["Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options",
                     "Strict-Transport-Security", "Referrer-Policy", "Permissions-Policy",
                     "Cross-Origin-Opener-Policy", "Cross-Origin-Resource-Policy",
                     "Cross-Origin-Embedder-Policy"],
        ),
        
        # Architecture
        KnowledgeSource(
            name="System Design Primer",
            url="https://github.com/donnemartin/system-design-primer",
            wing=Wing.ARCHITECTURE,
            room="system-design",
            description="Learn how to design large-scale systems",
            patterns=["load-balancing", "caching", "database", "cdn", "stateless",
                     "microservices", "event-driven", "message-queue", "logging",
                     "monitoring", "cache-patterns", "async-processing"],
        ),
        KnowledgeSource(
            name="12-Factor App",
            url="https://12factor.net",
            wing=Wing.ARCHITECTURE,
            room="12-factor",
            description="Methodology for building software-as-a-service",
            patterns=["codebase", "dependencies", "config", "backing-services", "build-release-run",
                     "processes", "port-binding", "concurrency", "disposability", "dev-prod-parity",
                     "logs", "admin-processes"],
        ),
        
        # Optimization
        KnowledgeSource(
            name="Web Vitals",
            url="https://web.dev/vitals",
            wing=Wing.OPTIMIZATION,
            room="web-vitals",
            description="Core Web Vitals optimization guide",
            patterns=["LCP", "FID", "CLS", "INP", "TTFB", "FCP", "interactive",
                     "largest-contentful-paint", "first-input-delay", "cumulative-layout-shift"],
        ),
        KnowledgeSource(
            name="Performance Patterns",
            url="https://web.devpatterns",
            wing=Wing.OPTIMIZATION,
            room="patterns",
            description="Web performance patterns",
            patterns=["code-splitting", "lazy-loading", "preloading", "caching",
                     "compression", "image-optimization", "font-optimization", "rendering"],
        ),
    ]
    
    def __init__(self):
        self.state_file = Path.home() / '.mempalace' / 'knowledge_gardener_state.json'
        self.state = self._load_state()
        self.client = None
        self.collection = None
        
        if CHROMA_AVAILABLE:
            try:
                self.client = chromadb.PersistentClient(path=PALACE_PATH)
                self.collection = self.client.get_or_create_collection(
                    name="knowledge_garden",
                    metadata={"description": "Deep domain knowledge from curated sources"}
                )
            except Exception as e:
                print(f"⚠️  ChromaDB init error: {e}")
    
    def _load_state(self) -> Dict:
        """Load gardener state."""
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text())
            except:
                pass
        return {"sources": {}, "last_full_scan": None}
    
    def _save_state(self):
        """Save gardener state."""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps(self.state, indent=2))
    
    def needs_mining(self, source: KnowledgeSource) -> bool:
        """Check if a source needs to be mined."""
        if source.name not in self.state["sources"]:
            return True
        
        last = self.state["sources"][source.name].get("last_mined")
        if not last:
            return True
        
        last_time = datetime.fromisoformat(last)
        if datetime.now() - last_time > timedelta(hours=source.frequency_hours):
            return True
        
        return False
    
    def fetch_knowledge(self, source: KnowledgeSource) -> List[Dict]:
        """Fetch knowledge from a source."""
        results = []
        
        if not CHROMA_AVAILABLE:
            return results
        
        # For GitHub sources, try to fetch
        if "github.com" in source.url:
            results.extend(self._fetch_github(source))
        
        # For web sources, try HTTP
        elif source.url.startswith("http"):
            results.extend(self._fetch_web(source))
        
        return results
    
    def _fetch_github(self, source: KnowledgeSource) -> List[Dict]:
        """Fetch from GitHub."""
        results = []
        
        try:
            import httpx
            
            # Convert raw GitHub URL to API URL
            api_url = source.url.replace("raw.githubusercontent.com", "api.github.com/repos")
            api_url = api_url.replace("/main/", "/contents/")
            
            headers = {"Accept": "application/vnd.github.v3+json"}
            if os.environ.get("GITHUB_TOKEN"):
                headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
            
            response = httpx.get(api_url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                content = response.text
                
                for pattern in source.patterns:
                    if pattern.lower() in content.lower():
                        results.append({
                            "source": source.name,
                            "pattern": pattern,
                            "wing": source.wing.value,
                            "room": source.room,
                            "content": content[:5000],
                            "url": source.url,
                        })
                        
        except Exception as e:
            print(f"  ⚠️  Fetch error: {e}")
        
        return results
    
    def _fetch_web(self, source: KnowledgeSource) -> List[Dict]:
        """Fetch from web."""
        results = []
        
        try:
            import httpx
            
            response = httpx.get(source.url, timeout=30, follow_redirects=True)
            
            if response.status_code == 200:
                content = response.text[:10000]  # First 10KB
                
                results.append({
                    "source": source.name,
                    "pattern": "index",
                    "wing": source.wing.value,
                    "room": source.room,
                    "content": content,
                    "url": source.url,
                })
                
        except Exception as e:
            print(f"  ⚠️  Web fetch error: {e}")
        
        return results
    
    def store_knowledge(self, knowledge: Dict):
        """Store knowledge in MemPalace."""
        if not self.collection:
            return
        
        doc_id = f"{knowledge['wing']}_{knowledge['room']}_{knowledge['pattern']}"
        doc_id = hashlib.md5(doc_id.encode()).hexdigest()[:16]
        
        try:
            self.collection.upsert(
                documents=[knowledge['content']],
                metadatas=[{
                    'source': knowledge['source'],
                    'wing': knowledge['wing'],
                    'room': knowledge['room'],
                    'pattern': knowledge['pattern'],
                    'url': knowledge.get('url', ''),
                    'stored_at': datetime.now().isoformat(),
                }],
                ids=[doc_id]
            )
        except Exception as e:
            print(f"  ⚠️  Storage error: {e}")
    
    def garden_source(self, source: KnowledgeSource) -> int:
        """Tend a single knowledge source."""
        if not self.needs_mining(source):
            return 0
        
        print(f"\n  🌱 Cultivating: {source.name}")
        print(f"     Wing: {source.wing.value} | Room: {source.room}")
        
        knowledge_list = self.fetch_knowledge(source)
        
        stored = 0
        for knowledge in knowledge_list:
            self.store_knowledge(knowledge)
            stored += 1
        
        # Update state
        self.state["sources"][source.name] = {
            "last_mined": datetime.now().isoformat(),
            "patterns_found": stored,
        }
        self._save_state()
        
        print(f"     ✓ Stored {stored} patterns")
        return stored
    
    def garden_all(self) -> Dict:
        """Tend all knowledge sources."""
        print("\n" + "=" * 60)
        print("D4RK MIND — KNOWLEDGE GARDENER")
        print("=" * 60)
        
        total_stored = 0
        sources_tended = 0
        
        for source in self.SOURCES:
            if self.needs_mining(source):
                stored = self.garden_source(source)
                total_stored += stored
                sources_tended += 1
            else:
                print(f"\n  ⏭️  Skipping (recently mined): {source.name}")
        
        self.state["last_full_scan"] = datetime.now().isoformat()
        self._save_state()
        
        return {
            "sources_tended": sources_tended,
            "patterns_stored": total_stored,
            "sources_total": len(self.SOURCES),
            "wings": list(set(s.wing.value for s in self.SOURCES)),
        }
    
    def list_sources(self):
        """List all configured knowledge sources."""
        print("\n" + "=" * 60)
        print("KNOWLEDGE SOURCES")
        print("=" * 60)
        
        by_wing = {}
        for source in self.SOURCES:
            if source.wing.value not in by_wing:
                by_wing[source.wing.value] = []
            by_wing[source.wing.value].append(source)
        
        for wing, sources in by_wing.items():
            print(f"\n  📁 {wing.upper()}")
            for source in sources:
                status = "✓" if not self.needs_mining(source) else "○"
                print(f"     {status} {source.name}")
                print(f"         Patterns: {len(source.patterns)}")
        
        print("\n" + "=" * 60)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='D4rk Mind — Knowledge Gardener')
    parser.add_argument('--daemon', '-d', action='store_true', help='Run forever')
    parser.add_argument('--sources', '-s', action='store_true', help='List knowledge sources')
    parser.add_argument('--interval', '-i', type=int, default=3600, help='Daemon interval (seconds)')
    parser.add_argument('--once', action='store_true', help='Run once then exit')
    
    args = parser.parse_args()
    
    gardener = KnowledgeGardener()
    
    if args.sources:
        gardener.list_sources()
        return
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║           D4rk Mind — Knowledge Gardener                    ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    if args.daemon:
        print("\n🌿 Running as daemon...")
        print(f"   Interval: {args.interval} seconds\n")
        
        while True:
            try:
                result = gardener.garden_all()
                print(f"\n✓ Tended {result['sources_tended']}/{result['sources_total']} sources")
                print(f"  Stored {result['patterns_stored']} patterns")
                print(f"  Wings: {', '.join(result['wings'])}")
                time.sleep(args.interval)
            except KeyboardInterrupt:
                print("\n\n👋 Garden paused.")
                break
    else:
        result = gardener.garden_all()
        print(f"\n" + "=" * 60)
        print("GARDENING COMPLETE")
        print("=" * 60)
        print(f"  Sources tended:    {result['sources_tended']}/{result['sources_total']}")
        print(f"  Patterns stored:    {result['patterns_stored']}")
        print(f"  Wings enriched:    {', '.join(result['wings'])}")
        print("=" * 60)


if __name__ == '__main__':
    main()
