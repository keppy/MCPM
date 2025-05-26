const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

console.log('🚀 Setting up MCPM - The MCP Package Manager...');

// Check for Python
try {
    const pythonVersion = execSync('python3 --version', { encoding: 'utf8' });
    console.log(`✓ Found ${pythonVersion.trim()}`);
} catch (e) {
    console.error('❌ Python 3 is required but not found in PATH');
    process.exit(1);
}

// Check for uv (optional but recommended)
try {
    execSync('uv --version', { encoding: 'utf8' });
    console.log('✓ Found uv - Installing dependencies with uv...');
    execSync('uv pip install -e .', { stdio: 'inherit' });
} catch (e) {
    console.log('⚡ uv not found, trying pip...');
    try {
        execSync('pip3 install aiohttp', { stdio: 'inherit' });
        console.log('✓ Dependencies installed with pip');
    } catch (pipError) {
        console.error('❌ Failed to install dependencies');
        process.exit(1);
    }
}

// Create bin wrapper
const binDir = path.join(__dirname, '..', 'bin');
if (!fs.existsSync(binDir)) {
    fs.mkdirSync(binDir);
}

const binScript = `#!/usr/bin/env node
const { spawn } = require('child_process');
const path = require('path');

const mcpmPath = path.join(__dirname, '..', 'mcpm.py');
const python = process.platform === 'win32' ? 'python' : 'python3';

const child = spawn(python, [mcpmPath, ...process.argv.slice(2)], {
    stdio: 'inherit',
    env: { ...process.env, PYTHONUNBUFFERED: '1' }
});

child.on('exit', (code) => {
    process.exit(code || 0);
});
`;

const binPath = path.join(binDir, 'mcpm');
fs.writeFileSync(binPath, binScript);
if (process.platform !== 'win32') {
    fs.chmodSync(binPath, '755');
}

// Create .mcpm directory
const mcpmHome = path.join(os.homedir(), '.mcpm');
if (!fs.existsSync(mcpmHome)) {
    fs.mkdirSync(mcpmHome, { recursive: true });
    console.log(`✓ Created MCPM home directory at ${mcpmHome}`);
}

console.log('\n✨ MCPM setup complete!');
console.log('💡 You can now use MCPM as an MCP server');
console.log('\n📝 Add to your MCP settings:');
console.log(JSON.stringify({
    "mcpm": {
        "command": "npx",
        "args": ["-y", "@keppylab/mcpm"]
    }
}, null, 2));
