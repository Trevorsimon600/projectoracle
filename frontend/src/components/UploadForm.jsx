import React from "react";

export default function UploadForm() {
  const [file, setFile] = React.useState(null);

  async function submit() {
    if (!file) return;
    const form = new FormData();
    form.append("file", file);
    await fetch("http://localhost:8000/uploads/?project_id=1", { method: "POST", body: form });
    alert("Uploaded");
  }

  return (
    <div>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={submit}>Upload</button>
    </div>
  );
}
