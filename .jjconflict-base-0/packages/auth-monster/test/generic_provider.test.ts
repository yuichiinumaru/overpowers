import { expect } from 'chai';
import { GenericProvider } from '../src/providers/generic';
import { ManagedAccount, AuthProvider } from '../src/core/types';

describe('GenericProvider', () => {
  const mockAccount: ManagedAccount = {
    id: 'test-generic',
    email: 'test@local',
    provider: AuthProvider.Generic,
    tokens: { accessToken: '' },
    isHealthy: true,
    metadata: {
      baseUrl: 'http://localhost:11434/v1'
    }
  };

  it('should generate correct URL from metadata', () => {
    const url = GenericProvider.getUrl('llama3', mockAccount);
    expect(url).to.equal('http://localhost:11434/v1/chat/completions');
  });

  it('should handle trailing slashes in baseUrl', () => {
    const accountWithSlash = { ...mockAccount, metadata: { baseUrl: 'http://localhost:11434/v1/' } };
    const url = GenericProvider.getUrl('llama3', accountWithSlash);
    expect(url).to.equal('http://localhost:11434/v1/chat/completions');
  });

  it('should fallback to localhost default if no baseUrl', () => {
    const accountNoBase = { ...mockAccount, metadata: {} };
    const url = GenericProvider.getUrl('llama3', accountNoBase);
    expect(url).to.equal('http://localhost:11434/v1/chat/completions');
  });

  it('should generate correct headers with apiKey', async () => {
    const accountWithKey = { ...mockAccount, apiKey: 'sk-test-123' };
    const headers = await GenericProvider.getHeaders(accountWithKey);
    expect(headers['Authorization']).to.equal('Bearer sk-test-123');
    expect(headers['Content-Type']).to.equal('application/json');
  });

  it('should include custom headers from metadata', async () => {
    const accountCustom = {
        ...mockAccount,
        metadata: {
            baseUrl: 'http://test',
            headers: { 'X-Custom-Auth': 'secret' }
        }
    };
    const headers = await GenericProvider.getHeaders(accountCustom);
    expect(headers['X-Custom-Auth']).to.equal('secret');
  });
});
