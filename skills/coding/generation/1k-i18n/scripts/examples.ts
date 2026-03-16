// ❌ NEVER modify these files - they are AUTO-GENERATED
// @onekeyhq/shared/src/locale/enum/translations.ts
// @onekeyhq/shared/src/locale/json/*.json

// ❌ NEVER hardcode text strings
<Text>Confirm</Text>

// ✅ CORRECT - Always use translation keys
import { ETranslations } from '@onekeyhq/shared/src/locale';
intl.formatMessage({ id: ETranslations.global__confirm })

import { useIntl } from 'react-intl';
import { ETranslations } from '@onekeyhq/shared/src/locale';

function MyComponent() {
  const intl = useIntl();

  return (
    <SizableText>
      {intl.formatMessage({ id: ETranslations.global__confirm })}
    </SizableText>
  );
}

import { appLocale } from '@onekeyhq/shared/src/locale/appLocale';
import { ETranslations } from '@onekeyhq/shared/src/locale';

const message = appLocale.intl.formatMessage({
  id: ETranslations.global__cancel,
});
