# Simulate network architectures with GNS3

## Emulation, Simulation and Virtualization

**A simulation imitates a situation**, like in a flight simulator. In the context of a network architecture, this means using a software (and not a physical machine) to model the network and compute/predict the corresponding events.

**An emulation reproduces identically the behavior of a network and its architecture**, without modeling, like in a GameBoy emulator. This means that the actual lines of codes will be executed, guaranteeing the same behavior/errors as obtained in reality.

**A virtualization is an emulation that uses the host architecture instead of reproducing another.** This yields performance gains. Virtualization of type I runs outside of the main OS, while virtualization of type II runs inside the main OS.

<br>

In this context, GNS3:
* **Simulates the behavior of two network interfaces connected** using an Ethernet wire
* **Emulates routers, switches and other servers**
* **Enables virtualization** of the most complex pieces