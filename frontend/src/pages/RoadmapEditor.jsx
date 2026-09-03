import React from "react";

function parseOutline(text) {
  // Very simple parser: lines starting with - or * or numbered create entries.
  const lines = text.split("\n").map(l => l.trim()).filter(Boolean);
  const items = [];
  lines.forEach(l => {
    items.push({ raw: l });
  });
  return items;
}

export default function RoadmapEditor() {
  const [text, setText] = React.useState(`# Life Goal\n- Become a stronger software engineer\n\n## Year Goal\n- Improve Python\n`);
  const [parsed, setParsed] = React.useState([]);

  function handleParse() {
    setParsed(parseOutline(text));
  }

  async function saveToServer() {
    // Here you'd call an API to save parsed roadmap (not implemented)
    await fetch("http://localhost:8000/roadmap/save", { method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify({text}) });
    alert("Saved (stub)");
  }

  return (
    <div>
      <h2>Roadmap Editor</h2>
      <textarea value={text} onChange={e => setText(e.target.value)} rows={12} cols={100} />
      <div>
        <button onClick={handleParse}>Parse</button>
        <button onClick={saveToServer}>Save</button>
      </div>
      <h3>Parsed</h3>
      <pre>{JSON.stringify(parsed, null, 2)}</pre>
    </div>
  );
}
