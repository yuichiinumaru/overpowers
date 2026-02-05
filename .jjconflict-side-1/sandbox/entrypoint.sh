#!/bin/bash
set -e

# Defaults
HOST_UID=${HOST_UID:-1000}
HOST_GID=${HOST_GID:-1000}
USER_NAME=${HOST_USER:-developer}
HOST_PASSWORD=${HOST_PASSWORD:-overpowers}

echo "🔮 Starting Overpowers Sandbox..."
echo "⚙️  Configuring user '$USER_NAME' with UID=$HOST_UID, GID=$HOST_GID..."

# Create Group
if ! getent group "$HOST_GID" >/dev/null; then
    groupadd -g "$HOST_GID" "$USER_NAME"
else
    # Group exists, likely 'users' or similar. We proceed.
    echo "   Group with GID $HOST_GID already exists."
fi

# Create User
if ! id -u "$HOST_UID" >/dev/null 2>&1; then
    # Create new user
    useradd -u "$HOST_UID" -g "$HOST_GID" -m -s /bin/zsh "$USER_NAME"
    echo "   User '$USER_NAME' created."
else
    # User exists (e.g. ubuntu), modify it
    EXISTING_USER=$(getent passwd "$HOST_UID" | cut -d: -f1)
    echo "   UID $HOST_UID matches existing user: $EXISTING_USER"
    if [ "$EXISTING_USER" != "$USER_NAME" ]; then
        if [ "$EXISTING_USER" == "ubuntu" ]; then
            usermod -l "$USER_NAME" -d /home/"$USER_NAME" -m ubuntu
            groupmod -n "$USER_NAME" ubuntu
            echo "   Renamed 'ubuntu' to '$USER_NAME'."
        else
             # Just use the existing user name if we can't rename
             USER_NAME=$EXISTING_USER
             echo "   Using existing username '$USER_NAME'."
        fi
    fi
fi

# Set password
echo "$USER_NAME:$HOST_PASSWORD" | chpasswd

# Passwordless Sudo
echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-developer

# Fix permissions
chown -R "$HOST_UID":"$HOST_GID" /home/"$USER_NAME"

# Update Supervisor Configs if they exist
if [ -d "/etc/supervisor/conf.d" ]; then
    sed -i "s/user=developer/user=$USER_NAME/g" /etc/supervisor/conf.d/*.conf
    sed -i "s|/home/developer|/home/$USER_NAME|g" /etc/supervisor/conf.d/*.conf
fi

echo "🚀 Sandbox Ready. Switching to supervisord..."
exec "$@"
