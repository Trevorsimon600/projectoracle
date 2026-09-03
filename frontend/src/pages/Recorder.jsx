import React from "react";

export default function Recorder() {
  const [message, setMessage] = React.useState("");

  function onSaved(data) {
    setMessage("Uploaded: " + JSON.stringify(data));
    if (Notification && Notification.permission === "granted") {
      new Notification("ORACLE", { body: "Video uploaded" });
    }
  }

  async function requestPermission() {
    if (Notification && Notification.permission !== "granted") {
      await Notification.requestPermission();
    }
  }

  React.useEffect(() => { requestPermission(); }, []);

  return (
    <div>
      <h2>Daily Video Log</h2>
      <VideoRecorder onSaved={onSaved} />
      <p>{message}</p>
    </div>
  );
}
