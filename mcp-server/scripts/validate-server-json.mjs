import { readFile } from "node:fs/promises";

import Ajv from "ajv";
import addFormats from "ajv-formats";

const metadataUrl = new URL("../server.json", import.meta.url);
const metadata = JSON.parse(await readFile(metadataUrl, "utf8"));
const schemaResponse = await fetch(metadata.$schema);

if (!schemaResponse.ok) {
  throw new Error(`Unable to load MCP Registry schema: HTTP ${schemaResponse.status}`);
}

const schema = await schemaResponse.json();
const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);

const validate = ajv.compile(schema);

if (!validate(metadata)) {
  console.error(JSON.stringify(validate.errors, null, 2));
  process.exit(1);
}

console.log(`Validated ${metadata.name} v${metadata.version} against ${metadata.$schema}`);
