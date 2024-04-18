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
          <Terminal data="Features" />
          {/* <Terminal id="dev-info-rt" /> */}
        </div>
      </div>
      <div className="right">
        <Terminal data="Keylogger.py - Info" />
        <Terminal data="Developer.cnf" />
      </div>
    </div>
  );
}

export default App;
