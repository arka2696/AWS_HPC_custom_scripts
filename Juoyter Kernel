### Creating custom jupyter kernels

```markdown
# Managing Jupyter Kernels

This document outlines useful commands for managing Jupyter kernels, including how to check which kernels are installed, remove kernels, and other related commands.

## Checking Installed Kernels

To see which kernels are installed (including those installed using `ipykernel`), run:

```bash
jupyter kernelspec list
```

This command lists all available kernels along with their installation paths.

## Removing a Kernel

To uninstall a specific kernel, use the following command:

```bash
jupyter kernelspec uninstall <kernel_name>
```

For example, to remove the kernel named `sam`, run:

```bash
jupyter kernelspec uninstall sam
```

## Other Useful Commands

### Installing a New Kernel

To install a new kernel with a custom name and display name, use:

```bash
python -m ipykernel install --user --name <env_name> --display-name "<display_name>"
```

For instance, to install a kernel named `sam`, run:

```bash
python -m ipykernel install --user --name sam --display-name "sam"
```

### Getting Help for ipykernel Install

For more details or options for installing kernels, check the help documentation:

```bash
python -m ipykernel install --help
```

### Viewing Jupyter Configuration Paths

To see where Jupyter looks for configuration files, kernels, etc., run:

```bash
jupyter --paths
```
```
