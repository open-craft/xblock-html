# HTML XBlock

A new HTML XBlock that is designed with security and embedding in mind. 

## Introduction
This XBlock fixes the existing HTML XModule in edX platform as it presents a number of problems when trying to embed it 
in another site (in particular, it often hosts content that depends on JS globals like jQuery being present, and it 
allows users to include arbitrary JavaScript).
