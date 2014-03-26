function showResult(tableName) {
	var QUERY = "select * from " + tableName
	
	STATUS_TEXT = "getting data from database..."

	doQuery(db, QUERY, function(tx, queryResult) {
		if (queryResult.rows.length == 0) {
			STATUS_TEXT = "No data"
			return;
		}
		var resultString = ""
		console.log(queryResult.rows.length);
		for (var i = 0; i < queryResult.rows.length; i++) {
			var row = queryResult.rows.item(i);
			resultString += JSON.stringify(row);
			resultString += '\n';
		}

		window.URL = window.URL || window.webkitURL;

		var blob = new Blob([resultString], {type: 'text/plain'});

		var a = document.createElement('a');
		a.href = window.URL.createObjectURL(blob);
		a.innerText = "Click to download"

		var download = document.getElementById("download")
		download.appendChild(a);

		STATUS_TEXT = "Done"

	});
}