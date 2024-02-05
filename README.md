# Simulated Queueing Network (SQN) Simulator

The Simulated Queueing Network (SQN) Model is a Python-based simulation tool designed to analyze and simulate queueing systems with multiple nodes, bins, and time constraints. One of the most approachable explanations for an SQN is its usage in simulating a factory assembly line, where .... This project provides a flexible and customizable framework for studying the behavior and performance of queueing networks in various scenarios. The synchronized queueing networks generated are formulated specifications of the General Semi-Markovian Process (GSMP) discrete-event model. The last section of this README describes the exact formulation.

## Why use an SQN?
A myriad of real-world scenarios can be effectively simulated using synchronized queueing networks, ranging from tangible examples like factory production to more abstract instances such as the protein synthesis pathway in Biology. Notably, simulating a factory assembly line stands out as a prominent application. In this context, the SQN Model is invaluable for faithfully replicating and comprehensively studying the intricate dynamics of the production process. Let's delve into how the SQN Model proves its worth in simulating a factory assembly line:

1. **Nodes Represent Production Stations:** Each node in the SQN corresponds to a production station on the assembly line. These nodes actively produce components or products and interact with each other through the flow of items.

2. **Bins Mimic Material Flow:** The bins associated with each node represent the containers or bins that store the produced items. These bins are not only indicators of the production state of a node but also play a crucial role in determining when a production node can start or resume its operation.

3. **Time Constraints and Synchronization:** The SQN introduces time constraints, ensuring a synchronized simulation of the factory assembly line. Time plays a critical role in the production process, and the SQN captures the temporal aspects, enabling the analysis of throughput, delays, and bottlenecks.

This project provides a flexible and customizable framework for studying the behavior and performance of queueing networks, from approachable examples such as the in various scenarios. Whether you're exploring the efficiency of a factory assembly line, analyzing the impact of different configurations, or optimizing resource allocation, the SQN Model empowers you to simulate and evaluate complex systems.



## Features

- **SQN Model Class**: The core of the project is the `SQN_Model` class, which allows users to define queueing network parameters such as the number of nodes, bins, maximum bin size, maximum time, and output map.
- **Simulation Engine**: The SQN Model includes a powerful simulation engine capable of running multiple trials and capturing essential metrics such as throughput, activity rate, and state history.
- **Configurability**: Users can easily configure simulation parameters and experiment with different network configurations and scenarios.
- **JSON Output**: Results from simulation trials can be packaged into a JSON format, facilitating easy storage, analysis, and sharing of simulation data.

## How It Works

The SQN Model simulates the behavior of a queueing network over time, where each node represents a stage in the queueing process, and bins represent the capacity of each node to handle incoming requests or tasks. The simulation progresses through discrete time steps, with events triggering transitions between nodes and bins.

Key functionalities of the SQN Model include:

- **State Transition Simulation**: The simulation engine handles state transitions within the queueing network based on predefined rules and event triggers. 
- **Event-Based Modeling**: Events such as generation timers and output selections drive the simulation forward, mimicking real-world queueing dynamics.
- **Metrics Collection**: The model collects important performance metrics such as throughput (task completion rate) and activity rate (percentage of active nodes) during the simulation.
- **Random SQN Generation**: Generation of random SQNs that fit all of the requirement for the SQN to be considered a General Semi-Markovian Process

## Getting Started

To get started with the SQN Model, follow these steps:

1. **Installation**: Clone the repository to your local machine.
2. **Configuration**: Customize simulation parameters such as the number of nodes, bins, and maximum time to suit your requirements.
3. **Run Simulations**: Execute the simulation script, specifying the desired number of repetitions and other parameters.
4. **Analyzing Results**: Review the output JSON file containing simulation results and metrics.

## Example Usage

```python
# Configure SQN Model parameters
debug = 0 # Altering this changes depth of information within the print display for state transitions
NUM_NODES = 5
NUM_BINS = 3
MAX_BIN = 10
MAX_TIME = 1000

# Create SQN Model instance
sim = SQN_Model(NUM_NODES, NUM_BINS, MAX_BIN, MAX_TIME, OUTMAP)

# Run simulation trials
num_reps = 10
trials = []
for rep in range(num_reps):
    trial = sim.do_rep(include_state_history=True, include_throughput=True)
    trials.append(trial)

# Analyze results
# Print or process simulation metrics as needed
