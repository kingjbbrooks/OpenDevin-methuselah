---
sidebar_label: process
title: opendevin.runtime.sandbox.docker.process
---

## DockerProcess Objects

```python
class DockerProcess(Process)
```

Represents a background command execution

#### \_\_init\_\_

```python
def __init__(id: int, command: str, result, pid: int)
```

Initialize a DockerProcess instance.

**Arguments**:

- `id` _int_ - The identifier of the command.
- `command` _str_ - The command to be executed.
- `result` - The result of the command execution.
- `pid` _int_ - The process ID (PID) of the command.

#### parse\_docker\_exec\_output

```python
def parse_docker_exec_output(logs: bytes) -> Tuple[bytes, bytes]
```

When you execute a command using `exec` in a docker container, the output produced will be in bytes. this function parses the output of a Docker exec command.

**Example**:

  Considering you have a docker container named `my_container` up and running
  $ docker exec my_container echo &quot;Hello OpenDevin!&quot;
  &gt;&gt; b&#x27;       Hello OpenDevin!&#x27;
  
  Such binary logs will be processed by this function.
  
  The function handles message types, padding, and byte order to create a usable result. The primary goal is to convert raw container logs into a more structured format for further analysis or display.
  
  The function also returns a tail of bytes to ensure that no information is lost. It is a way to handle edge cases and maintain data integrity.
  
  &gt;&gt; output_bytes = b&#x27;       Hello OpenDevin!&#x27;
  &gt;&gt; parsed_output, remaining_bytes = parse_docker_exec_output(output_bytes)
  
  &gt;&gt; print(parsed_output)
  b&#x27;Hello OpenDevin!&#x27;
  
  &gt;&gt; print(remaining_bytes)
  b&#x27;&#x27;
  

**Arguments**:

- `logs` _bytes_ - The raw output logs of the command.
  

**Returns**:

  Tuple[bytes, bytes]: A tuple containing the parsed output and any remaining data.

#### read\_logs

```python
def read_logs() -> str
```

Read and decode the logs of the command.

This function continuously reads the standard output of a subprocess and
processes the output using the parse_docker_exec_output function to handle
binary log messages. It concatenates and decodes the output bytes into a
string, ensuring that no partial messages are lost during reading.

Dummy Example:

&gt;&gt; cmd = &#x27;echo &quot;Hello OpenDevin!&quot;&#x27;
&gt;&gt; result = subprocess.Popen(
cmd, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.STDOUT, text=True, cwd=&#x27;.&#x27;
)
&gt;&gt; bg_cmd = DockerProcess(id, cmd = cmd, result = result, pid)

&gt;&gt; logs = bg_cmd.read_logs()
&gt;&gt; print(logs)
Hello OpenDevin!

**Returns**:

- `str` - The decoded logs(string) of the command.

