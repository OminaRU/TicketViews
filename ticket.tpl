<html>
  <head>
    <title>Coding Challenge</title>
    <link href="/css/main.css" rel="stylesheet">
  </head>
  <body>
      <h2>{{data['id']}}</h2>

      <p> Ticket subject: {{data['subject']}} </p>
      <p>  Job Status: {{data['status']}} </p>
  </body>

  <button onclick="goBack()">Back to all tickets</button>

<script>
function goBack() {
  window.history.back();
}
</script>
</html>
