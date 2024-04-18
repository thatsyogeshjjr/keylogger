import "../css/Terminal.css";

export var Terminal = () => {
  return (
    <div className="terminal">
      <div className="titlebar">
        <h2>Features</h2>
        <div className="title-buttons">
          <button className="t-btn green"></button>
          <button className="t-btn orange"></button>
          <button className="t-btn red"></button>
        </div>
      </div>
      <hr />
    </div>
  );
};
