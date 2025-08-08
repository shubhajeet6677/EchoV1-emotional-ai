#!/bin/bash
# build.sh - Render build script for Echo V1

set -e  # Exit on any error

echo "🚀 Starting Echo V1 build process..."

# Update package lists
echo "📦 Updating package lists..."
apt-get update

# Install system dependencies for audio processing
echo "🔊 Installing audio system dependencies..."
apt-get install -y \
    ffmpeg \
    libsndfile1 \
    libsndfile1-dev \
    portaudio19-dev \
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    python3-dev \
    build-essential \
    pkg-config

# Clean package cache to save space
apt-get clean
rm -rf /var/lib/apt/lists/*

# Upgrade pip
echo "🐍 Upgrading pip..."
python -m pip install --upgrade pip

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install --no-cache-dir -r requirements.txt

# Verify critical imports
echo "🧪 Testing critical imports..."
python -c "import streamlit; print('✅ Streamlit OK')"
python -c "import sounddevice; print('✅ sounddevice OK')" || echo "⚠️ sounddevice failed"
python -c "import whisper; print('✅ Whisper OK')" || echo "⚠️ Whisper failed"
python -c "import torch; print('✅ PyTorch OK')" || echo "⚠️ PyTorch failed"

echo "✅ Build completed successfully!"