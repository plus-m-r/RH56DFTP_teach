# RH56DFTP Python Library

A Python library for communicating with RH56DFTP devices (tactile hand) via Modbus TCP.

## Features

- Easy-to-use API for communicating with RH56DFTP tactile hand devices
- Support for reading and writing registers
- Built-in logging system for monitoring all operations
- Comprehensive register definitions including force, current, temperature, and error data
- Support for tactile data acquisition from all fingers and palm
- Modular design for easy extension

## Installation

### From Source

You can install the library from the GitHub repository:

```bash
git clone https://github.com/plus-m-r/RH56DFTP_teach.git
cd RH56DFTP_teach
pip install -e .
```

### From Local Package

After building the package, you can install it from the generated wheel file:

```bash
pip install dist/rh56dftp-0.1.0-py3-none-any.whl
```

## Requirements

- Python 3.7 or higher
- pymodbus 3.11.3

## Usage

### Basic Usage

```python
from RH56DFTP.RH56DFTP_TCP import RH56DFTP_TCP

# Initialize connection to the tactile hand
try:
    # Replace with your device's IP address and port
    client = RH56DFTP_TCP(host="192.168.123.210", port=6000)
    print("✅ Connected successfully to tactile hand")
    
    # Read device ID
    hand_id = client.get("HAND_ID")
    print(f"🤖 Hand ID: {hand_id}")
    
    # Write to a register (if supported)
    success = client.set("HAND_ID", 2)
    print(f"🔧 Set HAND_ID to 2: {success}")
    
    # Read force values from fingers
    for finger in range(6):
        force = client.get(f"FORCE_ACT({finger})")
        print(f"✋ Finger {finger} force: {force} g")
    
    # Close connection properly
    client.close()
    print("👋 Connection closed")
except Exception as e:
    print(f"❌ Error: {e}")
```

### Register Categories

The library provides predefined register names organized by function:

#### Device Configuration
- `HAND_ID`: Device ID (1-254)
- `REDU_RATIO`: Baud rate setting
- `CLEAR_ERROR`: Clear errors command
- `SAVE`: Save configuration to flash
- `RESET_PARA`: Restore factory settings

#### Finger Force Data (Read-only)
- `FORCE_ACT(0)`: Pinky finger force
- `FORCE_ACT(1)`: Ring finger force  
- `FORCE_ACT(2)`: Middle finger force
- `FORCE_ACT(3)`: Index finger force
- `FORCE_ACT(4)`: Thumb bending force
- `FORCE_ACT(5)`: Thumb rotation force

#### Actuator Data (Read-only)
- `CURRENT(0-5)`: Actuator current values (mA)
- `ERROR(0-5)`: Actuator error codes
- `TEMP(0-5)`: Actuator temperature values (°C)

#### Tactile Data (Read-only)
- Various tactile data registers for all fingers and palm
- 3x3, 12x8, and 10x8 matrix configurations
- 16-bit integer values (0-4096)

## Register Configuration

Register definitions are located in the `Register/config/configFTP` directory:
- `ftp_registers.py`: Main register configuration
- `ftp_registers_keys.py`: Register name constants

The library automatically loads these configurations during initialization.

## Logging

The library includes a built-in logging system that records:
- All `get` and `set` operations with timestamps
- Connection status and errors
- Register addresses and values

Logs are saved to `rh56dftp.log` and also printed to the console with the format:
```
YYYY-MM-DD HH:MM:SS - RH56DFTP - LEVEL - MESSAGE
```

## Project Structure

```
RH56DFTP_teach/
├── RH56DFTP/              # Main library code
│   ├── RH56DFTP_base.py   # Abstract base class
│   └── RH56DFTP_TCP.py    # TCP implementation
├── Register/              # Register configuration
│   ├── config/            # Configuration files
│   │   └── configFTP/     # FTP register configs
│   ├── RegisterKey/       # Register name constants
│   └── RegisterSet/       # Register classes
├── connect.py             # Example connection script
├── README.md              # This file
├── setup.py               # Package setup
└── requirements.txt       # Dependencies
```

## Development

### Building the Package

To build the package for distribution:

```bash
python setup.py sdist bdist_wheel
```

This will generate:
- `dist/rh56dftp-0.1.0.tar.gz` (source distribution)
- `dist/rh56dftp-0.1.0-py3-none-any.whl` (wheel distribution)

### Testing

Run the example script to test the connection:

```bash
python connect.py
```

## License

MIT License

## Repository

[https://github.com/plus-m-r/RH56DFTP_teach](https://github.com/plus-m-r/RH56DFTP_teach)
