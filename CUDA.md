Here is a detailed and well-structured Markdown file you can include in your GitHub repository. This guide explains how to properly install the NVIDIA CUDA Toolkit on **Ubuntu 22.04**, resolve keyring issues, and verify the installation.

---

````markdown
# Installing NVIDIA CUDA Toolkit on Ubuntu 22.04

This guide walks you through installing the NVIDIA CUDA Toolkit using `.deb` packages on Ubuntu 22.04. It includes steps to fix common issues like the `Signed-By` conflict and to verify a successful installation.

---

## Prerequisites

- Ubuntu 22.04 LTS
- NVIDIA GPU installed
- NVIDIA driver installed (run `nvidia-smi` to check)

---

## Step 1: Download the CUDA Keyring `.deb`

Download the official keyring package from NVIDIA:

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
````

Install the keyring:

```bash
sudo dpkg -i cuda-keyring_1.1-1_all.deb
```

---

## Step 2: Fix Signed-By Conflict (if it occurs)

If you encounter this error:

```text
E: Conflicting values set for option Signed-By regarding source https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /: ...
```

### 🛠 Solution:

Edit the CUDA source list:

```bash
sudo nano /etc/apt/sources.list.d/cuda.list
```

Replace any existing line with the following **correct format**:

```text
deb [signed-by=/usr/share/keyrings/cuda-archive-keyring.gpg] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /
```

Save (`Ctrl+O`, `Enter`) and exit (`Ctrl+X`).

---

## Step 3: Update Package List

```bash
sudo apt-get update
```

This should now work without any errors.

---

## Step 4: Install the CUDA Toolkit

To install the full toolkit:

```bash
sudo apt-get -y install cuda
```

You can also install specific versions, like:

```bash
sudo apt-get -y install cuda-12-3
```

Check available versions:

```bash
apt-cache search cuda-toolkit
```

---

## Step 5: Set Up Environment Variables

Add the following lines to your shell profile (e.g., `~/.bashrc` or `~/.zshrc`):

```bash
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

Then apply the changes:

```bash
source ~/.bashrc
```

---

## Step 6: Verify the Installation

### Check CUDA Toolkit version:

```bash
nvcc --version
```

### Check GPU status:

```bash
nvidia-smi
```

---

## Optional: Clean Up

Remove the downloaded `.deb` file if no longer needed:

```bash
rm cuda-keyring_1.1-1_all.deb
```

---

## References

* [NVIDIA CUDA Downloads](https://developer.nvidia.com/cuda-downloads)
* [NVIDIA Documentation](https://docs.nvidia.com/cuda/index.html)

---
GitHub no longer allows password-based authentication for Git operations over HTTPS — instead, you must use a **Personal Access Token (PAT)** or **SSH authentication**.

### ✅ Recommended Fix: Use a Personal Access Token (PAT)

1. **Generate a PAT**:

   * Go to: [https://github.com/settings/tokens](https://github.com/settings/tokens)
   * Click **"Generate new token" → "Classic"**
   * Select scopes like:

     * `repo` (for private repos)
   * Set an expiration date
   * Click **Generate Token** and **copy it** (you won’t see it again!)

2. **Clone using the token**:
   Replace your password with the token when prompted, or use this format in your terminal (not recommended for sharing/storing):

   ```bash
   git clone https://<your-username>:<your-token>@github.com/<your-username>/<repo-name>.git
   ```

   For you, that would be:

   ```bash
   git clone https://arka2696:<your-token>@github.com/arka2696/stellate-SAM.git
   ```

   Or better:

   * Use a **credential manager** to cache your token:

     ```bash
     git config --global credential.helper store
     ```

---

### 🔐 More Secure (Optional): Use SSH instead

If you want, I can guide you through setting up SSH keys and using `git@github.com:...` instead. Let me know!



```

Let me know if you'd like a more advanced version for installing CUDA in a headless server or HPC setting.
```
