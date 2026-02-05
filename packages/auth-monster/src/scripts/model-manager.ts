import { AuthMonster } from '../index';
import { ConfigManager } from '../core/config';
import { AuthProvider } from '../core/types';

const { Select, Form, List, Toggle } = require('enquirer');

export async function runModelManagerTUI() {
    console.log("\n=== 🤖 Auth Monster Model Manager ===\n");

    const configManager = new ConfigManager();
    const config = configManager.loadConfig();

    // Menu Principal
    const action = await new Select({
        name: 'action',
        message: 'What would you like to configure?',
        choices: [
            { name: 'personas', message: 'Manage Model Personas / Aliases' },
            { name: 'fallbacks', message: 'Configure Fallback Chains' },
            { name: 'exit', message: 'Exit' }
        ]
    }).run();

    if (action === 'exit') return;

    if (action === 'personas') {
        await managePersonas(config, configManager);
    } else if (action === 'fallbacks') {
        await manageFallbacks(config, configManager);
    }
}

async function managePersonas(config: any, manager: ConfigManager) {
    // Simples visualização por enquanto, expansível no futuro
    console.log("\n--- Current Managed Models ---");
    const models = Object.keys(config.modelPriorities || {});

    if (models.length === 0) {
        console.log("No custom model personas defined yet.");
    } else {
        models.forEach(m => console.log(`• ${m}`));
    }

    console.log("\n(Use 'fallback' option to define chains for these personas)");
}

async function manageFallbacks(config: any, manager: ConfigManager) {
    const modelName = await new Form({
        name: 'model',
        message: 'Define Fallback Chain',
        choices: [
            { name: 'alias', message: 'Model Alias (e.g. "sonnet")', initial: 'sonnet' },
            { name: 'chain', message: 'Fallback Chain (comma separated)', initial: 'claude-4.5-sonnet, gemini-3-pro' }
        ]
    }).run();

    if (modelName.alias && modelName.chain) {
        if (!config.modelPriorities) config.modelPriorities = {};

        const chain = modelName.chain.split(',').map((s: string) => s.trim().toLowerCase());
        config.modelPriorities[modelName.alias.toLowerCase()] = chain;

        manager.saveConfig(config);
        console.log(`\n✅ Updated chain for [${modelName.alias}]: ${chain.join(' -> ')}`);
    }
}

// Allow direct execution if run as script
if (require.main === module) {
    runModelManagerTUI().catch(console.error);
}
