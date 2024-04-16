document.getElementByXPath = function (sValue) {
  var a = this.evaluate(
    sValue,
    this,
    null,
    XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
    null
  );
  if (a.snapshotLength > 0) {
    return a.snapshotItem(0);
  }
};

document.getElementsByXPath = function (sValue) {
  var aResult = new Array();
  var a = this.evaluate(
    sValue,
    this,
    null,
    XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
    null
  );
  for (var i = 0; i < a.snapshotLength; i++) {
    aResult.push(a.snapshotItem(i));
  }
  return aResult;
};

function downloadTextAsFile(text, filename) {
  var blob = new Blob([text], { type: "text/plain" });
  var url = URL.createObjectURL(blob);
  var a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  URL.revokeObjectURL(url);
  document.body.removeChild(a);
}

function generateButton() {
  const samples = document.getElementsByXPath(
    '//span[@class="lang-ja"]//*[starts-with(@id,"pre-sample")]'
  );
  if (samples.length === 0) {
    return;
  }
  const h2EL = document.getElementByXPath('//span[@class="h2"]');
  const button = document.createElement("button");
  button.innerText = "テストケースのダウンロード";
  button.setAttribute("class", "btn btn-default btn-sm");
  button.addEventListener("click", function () {
    for (let i = 0; i < samples.length / 2; i++) {
      const input = samples[i * 2].textContent;
      const output = samples[i * 2 + 1].textContent;
      downloadTextAsFile(input, `input${i + 1}.txt`);
      downloadTextAsFile(output, `output${i + 1}.txt`);
    }
  });
  h2EL.appendChild(button);
}

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(generateButton, 100);
});
