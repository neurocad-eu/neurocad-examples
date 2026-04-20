const BASE_URL = process.env.BASE_URL || "https://sandbox.api.neurocad.eu";
const TOKEN = process.env.TOKEN || "replace-me";
const PROJECT_ID = process.env.PROJECT_ID || "prj_demo_001";

async function main() {
  const response = await fetch(`${BASE_URL}/v1/inference/jobs`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      project_id: PROJECT_ID,
      task: "field-inference",
      input: {
        material: "steel-a36",
        resolution: "medium",
      },
      labels: ["public-js-example"],
    }),
  });

  console.log(JSON.stringify(await response.json(), null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
