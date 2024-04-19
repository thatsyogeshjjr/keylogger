import "../css/Terminal.css";

export var Terminal = (props) => {
  var in_terminal = <></>;
  var img = "";
  if (props.data === "Features.txt") {
    img = "https://cdn-icons-png.flaticon.com/512/4341/4341118.png ";
    var index_count = 0;
    var data = [
      "Note keystroke logs down into a key.log file",
      "Send those files to a local server",
      "Encrypt the sent logs with a fernet key",
      "Encrypt the fernet keys with asymmetric encryption allowing only attacker to get access to logs",
      "A seperate file to generate public.pem, private.pem, and fernet.key for rsa and fernet encryption.",
    ];
    in_terminal = (
      <>
        <ul>
          {data.map((i) => {
            return <li>{i}</li>;
          })}
        </ul>
      </>
    );
  } else if (props.data === "Keylogger.py - Info") {
    img = "https://cdn-icons-png.flaticon.com/128/2538/2538026.png";
    in_terminal = (
      <>
        <p>
          Keylogger is malware, designed to record keystorkes of the victim
          machine.
        </p>
        <br />
        <strong>
          <p id="how-to">How to use?</p>
        </strong>
        <br />
        <ol>
          <li>
            <p>Install the packages required </p>
            <br />
            <code>pip install -r requirements.txt</code>
          </li>
          <li>
            <p>Generate the required keys for encryption</p> <br />
            <code>python gen_key.py</code>
          </li>
          <li>
            <p>Start the keylogger</p> <br />
            <code>python app.py</code>
          </li>
          <li>
            <p>To test exfil features</p> <br />
            <code>cd server</code>
            <br />
            <br />
            <code>python server.py</code>
          </li>
        </ol>
      </>
    );
  } else if (props.data === "Developer.cnf") {
    img = "https://cdn-icons-png.flaticon.com/128/8931/8931357.png";
    in_terminal = (
      <div className="dev-info">
        <h2>@thatsyogeshjjr</h2>
        <div className="social-imgs">
          <a href="https://github.com/thatsyogeshjjr" target="_blank">
            <img
              src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
              alt="Github"
              id="github-logo"
              class="socials"
            />
          </a>
          <a href="https://twitter.com/thatsyogeshjjr" target="_blank">
            <img
              src="data:image/png;base64,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"
              alt="X"
              id="x-logo"
              class="socials"
            />
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="terminal">
      <div className="titlebar">
        <div id="title-content">
          <img id="logo" src={img}></img>
          <h2> | {props.data}</h2>
        </div>
        <div className="title-buttons">
          <button className="t-btn green"></button>
          <button className="t-btn orange"></button>
          <button className="t-btn red"></button>
        </div>
      </div>
      <hr id="gap" />
      <div className="data">{in_terminal}</div>
    </div>
  );
};
