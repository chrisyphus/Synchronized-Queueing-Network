# Simulated Queueing Network (SQN) Simulator

The Simulated Queueing Network (SQN) Model is a Python-based simulation tool designed to analyze and simulate queueing systems with multiple nodes, bins, and time constraints. This project provides a flexible and customizable framework for studying the behavior and performance of queueing networks in various scenarios. The synchronized queueing networks generated are formulated specifications of the General Semi-Markovian Process (GSMP) discrete-event model. The last section of this README describes the exact formulation. For access to the powerpoint presentation/seminar for this work, please email me at cdgomez@umass.edu.

## Why use an SQN?
A myriad of real-world scenarios can be effectively simulated using synchronized queueing networks, ranging from tangible examples like factory production to more abstract instances such as the protein synthesis pathway in biology. Notably, simulating a factory assembly line stands out as a prominent application. In this context, the SQN Model is invaluable for faithfully replicating and comprehensively studying the intricate dynamics of the production process. Let's delve into how the SQN Model proves its worth in simulating a factory assembly line:

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

# Create estimator for future statistial analysis
estimator = Estimator(conf_pct=95, epsilon=0.01, relative=True)

# Run simulation trials
num_reps = 10
trials = []
for rep in range(num_reps):
    trial = sim.do_rep(include_state_history=True, include_throughput=True, estimator = estimator)
    trials.append(trial)

# Print or process simulation metrics as needed via changing debug

# Perform desired analysis. This can be done for more than the examples provided below.
print(estimator.get_mean())
print(estimator.get_variance())
print(estimator.get_conf_interval())

```

# **General Semi-Markovian Process (GSMP) Specification of SQN Model**

## **State Space**
$S \in \{(M_0, M_1, \dots, M_n)\} = \{ \{A_0\}, \{A_1, B_0, B_1, \dots B_{J1}\}, \dots \{A_n, B_0, B_1, \dots B_{Jn}\}\} \in \{\{1\}\} \times \{\{0, 1\} \times \{ 0, 1,\dots, U\}_0 \dots \{0, 1,\dots, U\}_{J1}\} \times \dots \{\{0, 1\} \times \{0, 1,\dots, U\}_0 \dots \{0, 1,\dots, U\}_{Jn}\}$

- $M_i$ represents a production node with $J$ incoming edges. Its state is $\{A_i, B_0, B_1, \dots B_{Ji}\}$ which represents whether it is actively producing and the number of 'parts' acquired in each bin
  - Each bin corresponds to one of the $J$ incoming edges.
- $A_i$ is 1 if currently producing and 0 if idle/waiting for parts.
- There is a universal maximum cap of $U$ number of parts for every bin.

## **Event Space**
- ${e_0} \in E(s)$
  - $ e_0 $ is the event representing the part completion for the source production node ($M_0$)
  - This event can always occur.
- $e_{i} \in E(s)$ if  $\sum_{j=0}^{J} I(B_j, M_i) == J$
  - Indicator function $I(B_j, M_i) == 1$ if bin $B_j \geq 1 $ for node $M_i$
  - Node $M_i$ can only begin production once all J of its bins are filled

## **Transition probabilities**
- $N(s, M_i)$ = $\sum_{j=0}^{n} I(s)$ with indicator function $I(s)$ == 1 if $M_i$ has an outgoing edge to $M_j$, this function totals all outgoing edges from arbitrary node $M_i$.
- $ p(s', s, e_i) = 1/N(s)$ with $s = (M_0(t), \dots, M_n(t))$ having an $M_i = (A_i, B_{0}, B_{1}, \dots, B_{Ji})$ with an $A_i = 1$ and an $M_j = (A_j, B_{0}, B_{1}, \dots, B_{Jj})$ with a $B_j = k$. The new state $s'$ has an $M_i = (A_i, B_{0}, B_{1}, \dots, B_{Ji})$ with an $A_i = 0$ and an $M_j = (A_j, B_{0}, B_{1}, \dots, B_{Jj})$ with a $B_j = k + 1$.
  - Upon node $M_{i}$'s completion of a new part (event $e_i$), node $M_i$ is marked as deactivated and then each of the nodes that has an incoming connection from $M_i$ has equal chance of being selected. On selection, the chosen node $M_j$ has the bin corresponding to $M_i$ incremented by 1.
- $p(s', s, e_0) = 1$ with $s = (M_1(t), \dots, M_n(t))$ having an $M_i = (0, k_0, k_1, \dots k_J)$ and $s' = (M_1(t),\dots, M_n(t))$ having an $M_i = (1, k_0-1, k_1-1, \dots k_J-1)$
  - Once an inactive node $M_i$ has at least 1 in all of its bins it is certain to become active and have all of its bins decremented by 1.

## **Clock Distribution Timers**
- $F(x; s', e', s, e^*) = F_p(x)$ with $F_p(x) = 1 - e^{-1/\beta x}$ being an exponential process with an average time of β minutes.
- For trials β was set to 0.5

## **Rate**
- $r(s, e) = 1$ for all $s$ and $e$

## **Initial State Distribution**
- $V(s_0) = \{M_0(0), M_1(0), \dots, M_n(0)\} = \{(A_0, (A_1, B_0, B_1, \dots, B_{J1}), \dots (A_n, B_0, B_1, \dots, B_{Jn})\} = \{\{1\}, \{0,0 \dots 0\}, \dots \{0,0 \dots 0\}\}$
  - Start with nothing produced, all nodes inactive and requiring each of its $J_i$ bins $\geq 1$ to begin production.
  - Note that every Node $M_i$ has a different number of incoming edges, so every $J_i$ varies per node.
  - The source node $M_0$ is always producing and has no incoming edges, hence A_0 is always 1 and it has no bins.

## $F(x; e_0, s_0) = F_{p}(x)$ defined above

