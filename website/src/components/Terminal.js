import "../css/Terminal.css";

export var Terminal = (props) => {
  var in_terminal = <></>;
  if (props.data === "Features") {
    in_terminal = (
      <>
        <table>
          <thead>
            <tr>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <input type="checkbox" checked="checked" />
              </td>
              <td>Note keystroke logs down into a key.log file</td>
            </tr>
            <tr>
              <td>
                <input type="checkbox" checked="checked" />
              </td>
              <td>Send those files to a local server (from server folder)</td>
            </tr>
            <tr>
              <td>
                <input type="checkbox" checked="checked" />
              </td>
              <td> encrypt the sent logs with a fernet key</td>
            </tr>
            <tr>
              <td>
                <input type="checkbox" checked="checked" />
              </td>
              <td>
                Encrypt the fernet keys with asymmetric encryption allowing only
                attacker to get access to logs
              </td>
            </tr>
            <tr>
              <td>
                <input type="checkbox" checked="checked" />
              </td>
              <td> encrypt the sent logs with a fernet key</td>
            </tr>
            <tr>
              <td>
                <input type="checkbox" checked="checked" />
              </td>
              <td>
                A seperate file to generate public.pem, private.pem, and
                fernet.key for rsa and fernet encryption.
              </td>
            </tr>
          </tbody>
        </table>
      </>
    );
  }

  return (
    <div className="terminal">
      <div className="titlebar">
        <h2>{props.data}</h2>
        <div className="title-buttons">
          <button className="t-btn green"></button>
          <button className="t-btn orange"></button>
          <button className="t-btn red"></button>
        </div>
      </div>
      <hr />
      {in_terminal}
    </div>
  );
};
