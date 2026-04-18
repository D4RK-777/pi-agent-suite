`2.1198297352756628` to `9.411498969440865` by switching counting sort to the observed value span |

Use `scripts/run-autoresearch-showcase.sh --list` to see the bundled launch targets, or run one or more showcases directly with the wrapper script.

## Results matrix

| Showcase | Baseline | Kept / best documented result | Delta |
|---|---:|---:|---:|
| OMX self-optimization | n/a | behavior-preserving cleanup | n/a |
| Kaggle-style tabular ML | 0.9458071278825997 AUC | 0.9976939203354298 AUC | +0.0518867924528301 |
| Noisy high-dimensional Bayes-opt | 2.833048700169374 | 4.75978993804531 | +1.926741237875936 |
| Latent subspace discovery | 3.7019658949006504 | 4.176124116152444 | +0.47415822125179353 |