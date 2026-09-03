import React from "react";
import Home from "./pages/Home";
import RoadmapEditor from "./pages/RoadmapEditor";
import Recorder from "./pages/Recorder";

export default function App() {
  const [route, setRoute] = React.useState("home");
  return (
    <div style={{ padding: 20 }}>
      <header>
        <h1>ORACLE — MVP</h1>
        <nav>
          <button onClick={() => setRoute("home")}>Home</button>
          <button onClick={() => setRoute("roadmap")}>Roadmap</button>
          <button onClick={() => setRoute("recorder")}>Recorder</button>
        </nav>
      </header>
      <main style={{ marginTop: 20 }}>
        {route === "home" && <Home />}
        {route === "roadmap" && <RoadmapEditor />}
        {route === "recorder" && <Recorder />}
      </main>
    </div>
  );
}
