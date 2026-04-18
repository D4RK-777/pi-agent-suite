orchestration cause**
3. **Measurement / artifact / assumption mismatch cause**

### Worker contract

Each worker must:
- own exactly one hypothesis lane
- gather evidence **for** and **against** the lane
- rank evidence strength
- call out missing evidence and failed predictions
- name the **critical unknown** for the lane
- recommend the best **discriminating probe**
- avoid collapsing into implementation

### Cross-check lenses

After the initial evidence pass, pressure-test with these lenses when relevant: