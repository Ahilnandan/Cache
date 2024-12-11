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
```
# Cache Simulator Documentation

## How It Works

The simulator processes memory access trace files and evaluates cache performance. It uses the following classes:

- **cache_builder**: Constructs the cache structure and manages cache sets.
- **my_set**: Represents an individual cache set and maintains a priority queue for LRU.
- **cache_operator**: Operates on the cache, handling hits, misses, and updates.

## Experiments Conducted

### Fixed Cache Design:
- 4-way set-associative cache.
- Cache size: 1024 KB.
- Block size: 4 bytes.
- Address size: 32 bits.

### Cache Size Variation:
- Cache sizes: 128 KB to 4096 KB.
- Observed and plotted miss rates for various trace files.

### Block Size Variation:
- Block sizes: 1 byte to 128 bytes (fixed 1024 KB cache size).
- Observed spatial locality effects.

### Associativity Variation:
- Associativity levels: 1-way to 64-way (fixed 1024 KB cache size).
- Evaluated hit rates for different trace files.

## Observations
- Certain trace files (e.g., `mcf.trace`) exhibit poor temporal and spatial locality, resulting in higher miss rates.
- Increasing block size improves spatial locality but reduces the number of cache lines.
- Associativity impacts vary by trace file, with diminishing returns at higher levels.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/Ahilnandan/Cache.git
    cd Cache
    ```

2. Run the simulator:
    ```bash
    python simulator.py
    ```

3. Ensure the required trace files are in the same directory.

## Graphical Results

The tool generates graphs for:
- Miss rate vs. cache size.
- Miss rate vs. block size.
- Hit rate vs. associativity.

These visualizations help in understanding cache behavior under different configurations.

## Trace Files

The simulator uses trace files containing memory access addresses. You can add your own trace files for testing. Place them in the working directory and ensure they follow the required format (one address per line).

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the tool or add new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or suggestions, please reach out via the repository's issue tracker.
