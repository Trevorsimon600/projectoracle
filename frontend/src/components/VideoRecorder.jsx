import React from "react";

export default function VideoRecorder({ onSaved }) {
  const mediaRef = React.useRef();
  const [recording, setRecording] = React.useState(false);
  const [mediaRecorder, setMediaRecorder] = React.useState(null);
  const [chunks, setChunks] = React.useState([]);

  React.useEffect(() => {
    async function init() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: true });
        mediaRef.current.srcObject = stream;
        const mr = new MediaRecorder(stream);
        mr.ondataavailable = (e) => setChunks(prev => [...prev, e.data]);
        mr.onstop = async () => {
          const blob = new Blob(chunks, { type: "video/webm" });
          const form = new FormData();
          form.append("file", blob, "log.webm");
          const res = await fetch("http://localhost:8000/recorder/video", { method: "POST", body: form });
          const data = await res.json();
          setChunks([]);
          onSaved && onSaved(data);
        };
        setMediaRecorder(mr);
      } catch (err) {
        console.error("Camera init failed", err);
      }
    }
    init();
    return () => {
      if (mediaRef.current && mediaRef.current.srcObject) {
        const tracks = mediaRef.current.srcObject.getTracks();
        tracks.forEach(t => t.stop());
      }
    };
  }, []);

  function start() {
    if (mediaRecorder) {
      mediaRecorder.start();
      setRecording(true);
    }
  }

  function stop() {
    if (mediaRecorder) {
      mediaRecorder.stop();
      setRecording(false);
    }
  }

  return (
    <div>
      <video ref={mediaRef} autoPlay muted style={{ width: 480, height: 360, background: "#000" }} />
      <div>
        <button onClick={start} disabled={recording}>Start</button>
        <button onClick={stop} disabled={!recording}>Stop & Upload</button>
      </div>
    </div>
  );
}
