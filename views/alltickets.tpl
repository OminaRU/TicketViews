<html>
  <head>
  	<style>
	table {
  		font-family: arial, sans-serif;
  		border-collapse: collapse;
  		width: 100%;
	}

	td, th {
  		border: 1px solid #dddddd;
  		text-align: left;
  		padding: 8px;
	}

	tr:nth-child(even) {
  		background-color: #dddddd;
	}
	</style>
     <title>Zendesk Profile Information</title>
     <link href="/css/main.css" rel="stylesheet">
	 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  </head>
  <body>
      <h2>List of all Tickets</h2>
	  <table id="data">
		<tr>
			<th>Subject</th>
			<th>Description</th>
		</tr>
		% for ticket in data:
		<tr>
			<td>{{ticket['subject']}}<br /><a href="showTicket/{{ticket['id']}}">Click me for more!</a></td>
			<td>{{ticket['description']}}</td>
		</tr>
		% end
		<script>
			$(document).ready(function(){
			$('#data').after('<div id="nav"></div>');
			var rowsShown = 25;
			var rowsTotal = $('#data tbody tr').length;
			numPages = rowsTotal/rowsShown;
			for(i = 0;i < numPages;i++) {
				var pageNum = i + 1;
				$('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
			}
			$('#data tbody tr').hide();
			$('#data tbody tr').slice(0, rowsShown).show();
			$('#nav a:first').addClass('active');
			$('#nav a').bind('click', function(){

			$('#nav a').removeClass('active');
			$(this).addClass('active');
			var currPage = $(this).attr('rel');
			var startItem = currPage * rowsShown;
			var endItem = startItem + rowsShown;
			$('#data tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
			css('display','table-row').animate({opacity:1}, 300);
			});
		});
		</script>
	  </table>
  </body>
</html>
