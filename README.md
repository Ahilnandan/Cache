# Cache Performance Simulator

This repository contains a Python-based simulation tool for analyzing cache performance in computer architecture. The simulator evaluates hit and miss rates for various cache configurations, including direct-mapped and set-associative caches. It is designed to help understand the impact of cache parameters such as size, block size, and associativity on performance.

## Features

- Simulates direct-mapped and set-associative caches.
- Configurable parameters:
  - **Cache size**
  - **Block size**
  - **Associativity**
- Implements **Least Recently Used (LRU)** replacement policy using a priority queue.
- Efficient memory usage with a modular design.
- Generates graphs to visualize results using **Matplotlib**.

## Requirements

- **Python 3.7+**
- Libraries:
  - `matplotlib`

Install dependencies using:

```bash
pip install matplotlib
