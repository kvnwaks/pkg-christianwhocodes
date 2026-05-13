# Setting Up a Programming Environment in Termux + Kali NetHunter

## 1. Install Termux

Install [Termux from F-Droid](https://f-droid.org/packages/com.termux/)

Avoid the Play Store version because it is outdated and lacks important updates.

---

## 2. Configure Android Permissions

Give Termux the following permissions/settings:

- Allow storage access
- Disable battery/background restrictions
- Allow unrestricted battery usage
- Enable “All files access” if available
- Enable "Disable child processes restrictions" in Developer Options if available

These help prevent Termux from being killed in the background and improve filesystem access.

---

## 3. Update Termux Packages

Run:

```bash
pkg update && pkg upgrade -y -o Dpkg::Options::="--force-confnew"
```

---

## 4. Install Required Termux Packages

Install the tools needed for the NetHunter environment:

```bash
pkg install wget mandoc proot -y
```

Install Neovim:

```bash
pkg install neovim -y
```

Enable Android storage access:

```bash
termux-setup-storage
```

---

## 5. Install Kali NetHunter Rootless

Download the installer:

```bash
wget -O install-nethunter-termux https://offs.ec/2MceZWr
```

Make it executable:

```bash
chmod +x install-nethunter-termux
```

Run the installer:

```bash
./install-nethunter-termux
```

During installation choose:

- Option `2` → Minimal installation
- `N` when asked to delete the existing rootfs

---

## 6. Start Kali NetHunter

Enter the Kali environment:

```bash
nh
```

---

## 7. Fix DNS Resolution

Edit `/etc/resolv.conf`:

```bash
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
echo "nameserver 1.1.1.1" >> /etc/resolv.conf
```

This helps fix internet and DNS issues inside the proot container.

---

## 8. Prevent systemd/dpkg Post-Install Errors

Because NetHunter runs inside a proot environment without real systemd support, some package scripts can fail.

Remove problematic post-install scripts:

```bash
rm -f /var/lib/dpkg/info/systemd.postinst
rm -f /var/lib/dpkg/info/systemd-sysv.postinst
rm -f /var/lib/dpkg/info/libsystemd0.postinst
rm -f /var/lib/dpkg/info/udev.postinst
```

---

## 9. Update Kali Packages

Update package lists:

```bash
apt update
```

Upgrade packages safely:

```bash
apt upgrade -y \
    -o Dpkg::Options::="--force-confnew" \
    -o Dpkg::Options::="--force-confdef"
```

Fix broken packages and clean up:

```bash
apt --fix-broken install -y \
    -o Dpkg::Options::="--force-confnew"

apt autoremove -y
```

---

## 10. Install Development Dependencies

Install common build tools and development headers:

```bash
apt install -y \
    build-essential \
    libffi-dev \
    python3-dev \
    libssl-dev \
    pkg-config \
    git \
    curl
```

These are commonly required when compiling Python packages with native extensions.

---

## 11. Install uv (Python Package Manager)

Install [uv by Astral](https://docs.astral.sh/uv/)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 12. Fix uv Hardlink Errors in Termux/NetHunter

Android and proot filesystems often do not support hardlinks correctly.

Configure `uv` to use copies instead:

```bash
mkdir -p ~/.config/uv

echo 'link-mode = "copy"' >> ~/.config/uv/uv.toml
```

This prevents errors such as:

```text
failed to hardlink file ... Operation not permitted
```

---

## 13. Configure GitHub SSH Authentication

Generate an SSH key:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

View the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output and add it to:

[GitHub SSH Keys Settings](https://github.com/settings/keys)

under **New SSH Key**.

---

## 14. Verify the Environment

Check installed tools:

```bash
python --version
gcc --version
git --version
uv --version
```

---

# Result

You now have a mobile Linux development environment with:

- Python
- GCC/build tools
- uv
- Git + SSH authentication
- Kali userspace inside Termux
- Neovim for editing

Suitable for:

- Backend development
- Python scripting
- CLI tooling
- Cybersecurity workflows
- Lightweight DevOps tasks
- Learning Linux from Android devices
