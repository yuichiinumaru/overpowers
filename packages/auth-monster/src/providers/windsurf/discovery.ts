
/**
 * Windsurf Extension Discovery & Analysis
 * 
 * dynamically analyzes the installed Windsurf extension.js to discover
 * Protobuf field numbers that may change between versions.
 */

import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';

// Default metadata fields if discovery fails (matches current spec/most common)
export const DEFAULT_METADATA_FIELDS = {
    api_key: 1,
    ide_name: 2,
    ide_version: 3,
    extension_version: 4,
    session_id: 5,
    locale: 6,
};

export type MetadataFields = typeof DEFAULT_METADATA_FIELDS;

let cachedFields: MetadataFields | null = null;

/**
 * Locate the Windsurf extension.js file
 */
function findExtensionFile(): string | null {
    const commonPaths = [
        // macOS
        '/Applications/Windsurf.app/Contents/Resources/app/extensions/windsurf/dist/extension.js',
        path.join(os.homedir(), 'Applications/Windsurf.app/Contents/Resources/app/extensions/windsurf/dist/extension.js'),
        // Linux
        '/usr/share/windsurf/resources/app/extensions/windsurf/dist/extension.js',
        path.join(os.homedir(), '.local/share/windsurf/resources/app/extensions/windsurf/dist/extension.js'),
        // Windows
        'C:\\Program Files\\Windsurf\\resources\\app\\extensions\\windsurf\\dist\\extension.js',
        path.join(os.homedir(), 'AppData\\Local\\Programs\\Windsurf\\resources\\app\\extensions\\windsurf\\dist\\extension.js'),
    ];

    for (const p of commonPaths) {
        if (fs.existsSync(p)) return p;
    }
    return null;
}

/**
 * Analyze extension.js content to find Metadata field numbers
 */
function parseMetadataFields(content: string): MetadataFields | null {
    // Look for field lists like: newFieldList(()=>[{no:1,name:"api_key",...},...])
    const fieldLists = [...content.matchAll(/newFieldList\(\(\)=>\[(.*?)\]\)/g)];

    for (const match of fieldLists) {
        const listContent = match[1];

        // The Metadata message must contain both api_key and ide_name
        // AND must NOT contain "event_name" (which indicates a telemetry message)
        if (listContent.includes('"api_key"') &&
            listContent.includes('"ide_name"') &&
            !listContent.includes('"event_name"')) {
            const fields = { ...DEFAULT_METADATA_FIELDS };

            // regex to extract {no:X,name:"field_name"}
            // Handles minified variations
            const extractField = (name: string) => {
                // pattern: {no:(\d+),name:"NAME"
                const regex = new RegExp(`{no:(\\d+),name:"${name}"`);
                const m = listContent.match(regex);
                return m ? parseInt(m[1], 10) : null;
            };

            const apiKey = extractField('api_key');
            const ideName = extractField('ide_name');

            if (apiKey && ideName) {
                fields.api_key = apiKey;
                fields.ide_name = ideName;

                // Try other fields
                const ideVersion = extractField('ide_version');
                if (ideVersion) fields.ide_version = ideVersion;

                const extVersion = extractField('extension_version');
                if (extVersion) fields.extension_version = extVersion;

                const sessionId = extractField('session_id');
                if (sessionId) fields.session_id = sessionId;

                const locale = extractField('locale');
                if (locale) fields.locale = locale;

                return fields;
            }
        }
    }

    return null;
}

/**
 * Get Metadata field mapping, using cached discovery or defaults
 */
export function getMetadataFields(): MetadataFields {
    if (cachedFields) return cachedFields;

    try {
        const extPath = findExtensionFile();
        if (extPath) {
            const content = fs.readFileSync(extPath, 'utf8');
            const discovered = parseMetadataFields(content);
            if (discovered) {
                cachedFields = discovered;
                return cachedFields;
            }
        }
    } catch (error) {
        throw new Error('[Windsurf] Failed to discover extension fields: ' + error);
    }

    // Fallback to default
    cachedFields = DEFAULT_METADATA_FIELDS;
    return cachedFields;
}
