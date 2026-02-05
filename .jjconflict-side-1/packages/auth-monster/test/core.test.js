const { expect } = require('chai');
const { AccountRotator } = require('../src/core/rotation');
const { UnifiedModelHub } = require('../src/core/hub');
const { AuthProvider } = require('../src/core/types');
const { isOnCooldown, applyCooldown, preflightCheck } = require('../src/core/quota-manager');

describe('Core Components', () => {

    describe('AccountRotator', () => {
        let rotator;
        let accounts;

        beforeEach(() => {
            rotator = new AccountRotator();
            accounts = [
                { id: '1', provider: AuthProvider.Gemini, email: '1@test.com', tokens: {}, isHealthy: true, healthScore: 100 },
                { id: '2', provider: AuthProvider.Gemini, email: '2@test.com', tokens: {}, isHealthy: true, healthScore: 90 },
                { id: '3', provider: AuthProvider.Gemini, email: '3@test.com', tokens: {}, isHealthy: true, healthScore: 80 }
            ];
        });

        it('should select account using round-robin', () => {
            const first = rotator.selectAccount(accounts, 'round-robin');
            const second = rotator.selectAccount(accounts, 'round-robin');
            const third = rotator.selectAccount(accounts, 'round-robin');

            expect(first).to.not.be.null;
            expect(second).to.not.be.null;
            expect(third).to.not.be.null;

            const selectedIds = new Set([first.id, second.id, third.id]);
            expect(selectedIds.size).to.equal(3);
        });

        it('should skip unhealthy accounts', () => {
            accounts[1].isHealthy = false;

            const selected = [];
            for(let i=0; i<5; i++) {
                selected.push(rotator.selectAccount(accounts, 'round-robin'));
            }

            const selectedIds = selected.map(a => a.id);
            expect(selectedIds).to.not.include('2');
        });
    });

    describe('UnifiedModelHub', () => {
        let hub;
        let accounts;

        beforeEach(() => {
            hub = new UnifiedModelHub();
            accounts = [
                { id: '1', provider: AuthProvider.Gemini, email: 'gemini@test.com', tokens: {}, isHealthy: true, healthScore: 100 },
                { id: '2', provider: AuthProvider.Anthropic, email: 'claude@test.com', tokens: {}, isHealthy: true, healthScore: 100 },
                { id: '3', provider: AuthProvider.Windsurf, email: 'windsurf@test.com', tokens: {}, isHealthy: true, healthScore: 100 }
            ];
        });

        it('should resolve gemini-3-flash-preview to Gemini or Windsurf', () => {
            const selection = hub.selectModelAccount('gemini-3-flash-preview', accounts);
            expect(selection).to.not.be.null;
            expect([AuthProvider.Gemini, AuthProvider.Windsurf]).to.include(selection.provider);
            expect(selection.modelInProvider).to.equal('gemini-3-flash');
        });

        it('should fallback if primary provider is missing', () => {
            const onlyWindsurf = accounts.filter(a => a.provider === AuthProvider.Windsurf);
            const selection = hub.selectModelAccount('gemini-3-flash-preview', onlyWindsurf);
            expect(selection).to.not.be.null;
            expect(selection.provider).to.equal(AuthProvider.Windsurf);
        });

        it('should return null for unknown model', () => {
            const selection = hub.selectModelAccount('unknown-model', accounts);
            expect(selection).to.be.null;
        });
    });

    describe('QuotaManager', () => {
        it('should track cooldowns', () => {
            const accountId = 'test-id';
            const provider = AuthProvider.Gemini;

            expect(isOnCooldown(provider, accountId)).to.be.false;

            applyCooldown(provider, accountId, 1); // 1 minute

            expect(isOnCooldown(provider, accountId)).to.be.true;
        });

        it('should preflight check allow valid account', () => {
            const currentAccount = { id: '1', provider: AuthProvider.Gemini, email: '1@test.com', tokens: {}, isHealthy: true, healthScore: 100, quota: { remaining: 100 } };
            const allAccounts = [currentAccount];

            const result = preflightCheck(AuthProvider.Gemini, currentAccount, allAccounts);
            expect(result.proceed).to.be.true;
            expect(result.accountId).to.equal('1');
        });

        it('should preflight check switch if account has no quota', () => {
            const currentAccount = { id: '1', provider: AuthProvider.Gemini, email: '1@test.com', tokens: {}, isHealthy: true, healthScore: 100, quota: { remaining: 0 } };
            const healthyAccount = { id: '2', provider: AuthProvider.Gemini, email: '2@test.com', tokens: {}, isHealthy: true, healthScore: 100, quota: { remaining: 100 } };
            const allAccounts = [currentAccount, healthyAccount];

            const result = preflightCheck(AuthProvider.Gemini, currentAccount, allAccounts);
            expect(result.proceed).to.be.true;
            expect(result.accountId).to.equal('2');
            expect(result.switchedFrom).to.equal('1');
        });
    });
});
