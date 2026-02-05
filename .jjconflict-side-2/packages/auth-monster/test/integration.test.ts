const { expect } = require('chai');
const { UnifiedModelHub } = require('../src/core/hub');
const { AuthProvider } = require('../src/core/types');
const { SecretStorage } = require('../src/core/secret-storage');
const { CostEstimator } = require('../src/core/cost-estimator');
const { AuthMonster } = require('../src/index');
const path = require('path');
const fs = require('fs');
const os = require('os');

describe('Integration Phases', () => {
    let tempDir: any;

    before(() => {
        tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'auth-monster-test-'));
    });

    after(() => {
        fs.rmSync(tempDir, { recursive: true, force: true });
    });

    describe('Phase 1: Secure Storage', () => {
        it('should instantiate SecretStorage', () => {
            const secretStorage = new SecretStorage(tempDir);
            expect(secretStorage).to.be.instanceOf(SecretStorage);
        });

        it('should save and retrieve secret (fallback mode)', async () => {
            const secretStorage = new SecretStorage(tempDir);
            await secretStorage.saveSecret('testService', 'testAccount', 'secretValue');
            const retrieved = await secretStorage.getSecret('testService', 'testAccount');
            expect(retrieved).to.equal('secretValue');
        });
    });

    describe('Phase 2: Providers', () => {
        it('should have new providers in AuthProvider enum', () => {
            expect(AuthProvider.Azure).to.equal('azure');
            expect(AuthProvider.Grok).to.equal('grok');
            expect(AuthProvider.DeepSeek).to.equal('deepseek');
        });

        it('should instantiate UnifiedModelHub with new mappings', () => {
            const hub = new UnifiedModelHub();
            expect(hub).to.be.instanceOf(UnifiedModelHub);
        });
    });

    describe('Phase 3: Traffic & Cost', () => {
        it('should calculate cost', () => {
            const cost = CostEstimator.calculateCost('gpt-4o', 1000000, 1000000);
            expect(cost).to.be.greaterThan(0);
        });
    });

    describe('Phase 4 & 5: UI & Workflows', () => {
        it('should instantiate AuthMonster', () => {
            const monster = new AuthMonster({
                config: { active: AuthProvider.Gemini },
                storagePath: tempDir
            });
            expect(monster).to.be.instanceOf(AuthMonster);
        });
    });
});
