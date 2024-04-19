import "./css/App.css";
import { Header } from "./Header.js";
import { Terminal } from "./components/Terminal.js";

function App() {
  return (
    <div className="App">
      <div className="left">
        <div className="title">
          <Header />
        </div>
        <div className="terminals">
          <Terminal data="Features.txt" />
          <br />
          <br />
          <br />
          <div className="proj-link">
            <h2>Visit the project at GitHub</h2>({" "}
            <a
              href="https://github.com/thatsyogeshjjr/keylogger"
              target="_blank"
            >
              thatsyogeshjjr/Keylogger
            </a>{" "}
            )
          </div>
        </div>
      </div>
      <div className="right">
        <Terminal
          className="info-terminal rt-terminal"
          data="Keylogger.py - Info"
        />
        <Terminal className="dev-terminal rt-terminal" data="Developer.cnf" />
      </div>
    </div>
  );
}

export default App;
