import { expect } from 'chai';
import { CookieManager } from '../../../src/integrations/codexbar/cookie-manager';

describe('CookieManager Integration', () => {
  it('should return null (graceful failure) when cookies are not found in sandbox', async () => {
    // We expect this to fail or return null, but not throw.
    const cookies = await CookieManager.getCookiesForDomain('example.com');
    expect(cookies).to.be.null;
  });
});
