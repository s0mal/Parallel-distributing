# Basic Python Codes

This repository contains basic Python programs designed to demonstrate fundamental programming concepts and advanced techniques like parallel computing, threading, multiprocessing, and GPU computing. Each file highlights specific concepts and functionalities relevant to beginner and intermediate Python programmers.

## Contents

### 1. **calculator.py**
A simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division). Users can input two numbers and choose the desired operation.

### 2. **data_structures.py**
This file demonstrates the use of various data structures in Python, including:
- Tuples
- Lists
- Dictionaries

Examples and explanations are provided to help understand how to use these data structures effectively.

### 3. **functions.py**
This script showcases how to define and use functions in Python. It includes examples of:
- Defining functions
- Function parameters and return values
- Calling functions

### 4. **classes.py**
This file introduces object-oriented programming (OOP) in Python. It covers:
- Creating classes and objects
- Defining methods
- Using inheritance

### 5. **mpi_example.py**
This script demonstrates how to use **MPI** (Message Passing Interface) for distributed computing with **mpi4py**. It shows basic communication between processes:
- Sending and receiving data using MPI
- Handling process ranks and sizes

### 6. **multiprocessing_vs_threading.py**
This script compares multiprocessing and threading for concurrent programming:
- **Multiprocessing**: Using Python’s `multiprocessing` module to spawn multiple processes.
- **Multithreading**: Using Python’s `threading` module to spawn multiple threads.

It measures and compares execution times for both techniques using a basic list processing task.

### 7. **gpu_computation.py**
Demonstrates how to leverage **GPU** for parallel computing using **Numba**'s CUDA JIT compiler:
- Vector addition using GPU for accelerated computation
- Verifying the result using Numba’s CUDA capabilities.

### 8. **num_parallel_computing.py**
This script demonstrates vector addition using data parallelism with **NumPy**:
- Simple vector addition to compute the result using NumPy's optimized parallelism.
- Measures and prints execution time for large vector sizes.

### 9. **threadpool_executor.py**
Illustrates the use of **ThreadPoolExecutor** to manage a pool of threads for concurrent execution of tasks:
- Demonstrates executing multiple tasks in parallel with a thread pool.
- Uses `ThreadPoolExecutor` to run functions asynchronously.

### 10. **producer_consumer.py**
This script demonstrates the producer-consumer problem using **multiprocessing**:
- Two processes, `producer` and `consumer`, communicate via a `Queue`.
- The producer produces items and the consumer consumes them.

### 11. **semaphore_example.py**
This script demonstrates how to use a **semaphore** to control access to a shared resource with threading:
- Controls access to a resource by limiting the number of concurrent threads that can access it.

### 12. **multiprocessing_example.py**
Demonstrates **multiprocessing** with basic process spawning:
- Executes two functions (print square and print cube) in parallel using separate processes.
- Shows process synchronization and joining.

### 13. **fibonacci_threading.py**
Illustrates using multiple threads to calculate Fibonacci numbers:
- Uses **threading** to calculate Fibonacci numbers concurrently.

### 14. **threading_event_example.py**
Demonstrates **threading events** for communication between threads:
- Producer creates random numbers, and consumer consumes them using an event to synchronize operations.

### 15. **lock_example.py**
Shows how to use **thread locks** for synchronization in multithreading:
- Locks prevent race conditions by ensuring only one thread can access a shared resource at a time.

---

## Chapter 3: Process Management and Communication

This chapter explores various concepts and Python implementations related to process management, interprocess communication (IPC), and process synchronization. It covers examples that demonstrate how processes communicate using pipes, queues, and barriers, as well as handling processes in the background, killing processes, and managing process pools.

### 1. **communicating_with_pipe.py**
This script demonstrates interprocess communication using pipes to send data between processes.

### 2. **communicating_with_queue.py**
Demonstrates interprocess communication using queues to exchange data between processes.

### 3. **derom.py**
Implements a simple program related to process communication or management.

### 4. **killing_processes.py**
Demonstrates how to terminate running processes using Python.

### 5. **myFunc.py**
Defines a function or process-related code to be executed by processes.

### 6. **naming_processes.py**
Demonstrates the naming of processes and how to retrieve process names.

### 7. **process_in_subclass.py**
Shows how to subclass the Process class to create custom process implementations.

### 8. **process_pool.py**
Implements a process pool for concurrent execution of tasks using the Pool class.

### 9. **processes_barrier.py**
Demonstrates how to use barriers to synchronize processes and ensure they proceed together.

### 10. **run_background_processes.py**
Demonstrates how to run processes in the background.

### 11. **run_background_processes_no_daemons.py**
Shows how to run background processes that are not daemonized, meaning they do not exit when the main program ends.

### 12. **spawning_processes.py**
Demonstrates how to spawn new processes and manage their execution.

### 13. **spawning_processes_namespace.py**
Demonstrates how to use multiprocessing with a namespace to share data between processes.

---

## Chapter 4: Message Passing

This chapter focuses on demonstrating message-passing techniques using **MPI (Message Passing Interface)** with the **mpi4py** library in Python. The examples in this chapter showcase how to manage communication between multiple processes in a parallel computing environment. Key concepts include sending and receiving data between processes, using collective communication, and understanding Cartesian topology for process communication.

### 1. **basic_mpi_example.py**
This script demonstrates basic **MPI** communication using the **mpi4py** library.

### 2. **collective_communication.py**
This example illustrates the use of **collective communication** in MPI, using the `gather` function to collect data from all processes and send it to the root process.

### 3. **cartesian_topology_example.py**
This script demonstrates the use of **Cartesian topology** for process communication in a 2D grid using MPI’s `Create_cart` method.

---

## Chapter 5: Asynchronous Programming in Python

This chapter contains multiple examples of asynchronous programming in Python using the `asyncio` module. The examples showcase how to manage event loops, run multiple coroutines, use `asyncio.Future` for coordination between tasks, and simulate a finite state machine. These examples help in understanding the concept of asynchronous programming and its application in real-world problems.

### 1. **Managing Event Loop**
In this example, we demonstrate how to create an event loop that schedules tasks (`task_A`, `task_B`, and `task_C`) to run at specified times.

### 2. **Running Multiple Coroutines**
This example shows how to run multiple coroutines concurrently using `asyncio.create_task` and `asyncio.gather`.

### 3. **Using asyncio.Future for Two Coroutines**
This example demonstrates the use of `asyncio.Future` to coordinate two coroutines and retrieve their results once both tasks are completed.

### 4. **Finite State Machine Simulation**
In this example, we simulate a finite state machine using `asyncio`, where the system transitions between different states based on input values.

---

## Requirements

To run these scripts, you need Python 3.x and some external libraries:
- `mpi4py` for MPI examples
- `numba` and `numpy` for GPU computing examples
- `concurrent.futures` for ThreadPoolExecutor
- `multiprocessing` and `threading` for concurrent and parallel programming examples
- `asyncio` for asynchronous programming examples

You can install the required libraries using:

```bash
pip install mpi4py numba numpy
