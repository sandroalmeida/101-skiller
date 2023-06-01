skill_patterns = {

    #(1) Java
    "java": [{"LOWER": "java"}],
    "jee": [{"LOWER": "jee"}],
    "j2ee": [{"LOWER": "j2ee"}],
    
    #(2) Python
    "python": [{"LOWER": "python"}],
    
    #(3) CSharp
    "csharp": [{"LOWER": "csharp"}],
    "c sharp": [{"LOWER": "c"}, {"LOWER": "sharp"}],
    "c#": [{"LOWER": "c"},{"TEXT": {"REGEX": "#"}}],
    
    #(4) Objective C
    "objective-c": [{"LOWER": "objective"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "c"}],
    "objectivec": [{"LOWER": "objectivec"}],
    "objective.c": [{"LOWER": "objective.c"}],
    
    #(5) Golang
    "go": [{"IS_TITLE": True, "LOWER": "go"}],
    "golang": [{"LOWER": "golang"}],
    "go programming": [{"LOWER": "go"}, {"LOWER": "programming"}],
    "go (programming": [{"LOWER": "go"}, {"LOWER": "("}, {"LOWER": "programming"}],
    "go language": [{"LOWER": "go"}, {"LOWER": "language"}],
    "go (language": [{"LOWER": "go"}, {"LOWER": "("}, {"LOWER": "language"}],
    
    #(6) Kotlin
    "kotlin": [{"LOWER": "kotlin"}],

    #(7) Rust
    "rust": [{"LOWER": "rust"}],

    #(8) VB.Net
    "vb.net": [{"LOWER": "vb.net"}],
    "visual basic": [{"LOWER": "visual"}, {"LOWER": "basic"}],
    "vb": [{"LOWER": "vb"}],
    "vb .net": [{"LOWER": "vb"}, {"LOWER": ".net"}],
    "vb net": [{"LOWER": "vb"}, {"LOWER": "net"}],
    "vbnet": [{"LOWER": "vbnet"}],

    #(9) ASP.Net
    "asp.net": [{"LOWER": "asp.net"}],
    "aspnet": [{"LOWER": "aspnet"}],
    "asp .net": [{"LOWER": "asp"}, {"LOWER": ".net"}],
    "asp net": [{"LOWER": "asp"}, {"LOWER": "net"}],
    
    #(10) Bash
    "bash": [{"LOWER": "bash"}],

    #(11) Visual Basic
    "visual basic 6": [{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": "6"}],
    "vb6": [{"LOWER": "vb6"}],
    "vb 6": [{"LOWER": "vb"}, {"LOWER": "6"}],

    #(12) C
    "c" : [{"LOWER": {"NOT_IN": ["objective", "-", "quite", "exactly"]}}, {"LOWER": "c"}, {"LOWER": {"NOT_IN": ["sharp", "+", "#", ".net", "dotnet", "dot", "-", "shell", "*"]}}],

    #(13) C++
    "c++": [{"LOWER": "c++"}],
    "c ++": [{"LOWER": "c"}, {"LOWER": "++"}],
    "c + +": [{"LOWER": "c"}, {"LOWER": "+"}, {"LOWER": "+"}],

    #(14) CSS
    "css": [{"LOWER": "css"}],
    "css3": [{"LOWER": "css3"}],

    #(15) GraphQL
    "graphql": [{"LOWER": "graphql"}],

    #(16) HTML
    "html": [{"LOWER": "html"}],
    "html5": [{"LOWER": "html5"}],

    #(17) Javascript
    "javascript": [{"LOWER": "javascript"}],
    "java script": [{"LOWER": "java"}, {"LOWER": "script"}],
    "js": [{"LOWER": "js"}],

    #(18) Linq
    "linq": [{"LOWER": "linq"}],
    "language integrated query": [{"LOWER": "language"}, {"LOWER": "integrated"}, {"LOWER": "query"}],

    #(19) Matlab
    "matlab": [{"LOWER": "matlab"}],
    "mat lab": [{"LOWER": "mat"}, {"LOWER": "lab"}],

    #(20) NodeJS
    "nodejs": [{"LOWER": "nodejs"}],
    "node.js": [{"LOWER": "node.js"}],
    "node js": [{"LOWER": "node"}, {"LOWER": "js"}],

    #(21) Perl
    "Perl": [{"LOWER": "perl"}],

    #(22) PHP
    "PHP": [{"LOWER": "php"}],

    #(23) Ruby
    "Ruby": [{"LOWER": "ruby"}],
    "Rubyonrails": [{"LOWER": "rubyonrails"}],
    "Ruby onrails": [{"LOWER": "ruby"}, {"LOWER": "onrails"}],
    "Ruby on rails": [{"LOWER": "ruby"}, {"LOWER": "on"}, {"LOWER": "rails"}],

    #(24) Scala
    "Scala": [{"LOWER": "scala"}],

    #(25) SASS
    "SASS": [{"LOWER": "sass"}],

    #(26) Shell
    "Shell": [{"LOWER": "shell"}],

    #(27) Powershell
    "Powershell": [{"LOWER": "powershell"}],

    #(28) Swift
    "Swift": [{"LOWER": "swift"}],

    #(29) R
    "r" : [{"LOWER": "r"}, {"LOWER": {"NOT_IN": ["+"]}}],

    #(30) Typescript
    "typescript": [{"LOWER": "typescript"}],
    "type script": [{"LOWER": "type"}, {"LOWER": "script"}],

    #(31) SQL
    "sql": [{"LOWER": "sql"}],
    "tsql": [{"LOWER": "tsql"}],
    "plsql": [{"LOWER": "plsql"}],

    #(32) ADO.NET
    "ado.net": [{"LOWER": "ado.net"}],
    "adonet": [{"LOWER": "adonet"}],
    "ado net": [{"LOWER": "ado"}, {"LOWER": "net"}],
    "ado .net": [{"LOWER": "ado"}, {"LOWER": ".net"}],

    #(33) AJAX
    "asynchronous javaScript and xml": [{"LOWER": "asynchronous"}, {"LOWER": "javascript"}, {"LOWER": "and"}, {"LOWER": "xml"}],
    "ajax": [{"LOWER": "ajax"}],

    #(34) Angular
    "angular": [{"LOWER": "angular"}],
    "angular2": [{"LOWER": "angular2"}],

    #(35) Angular.JS
    "angularjs": [{"LOWER": "angularjs"}],
    "angular.js": [{"LOWER": "angular.js"}],

    #(36) Apache Spark
    "spark": [{"LOWER": "spark"}],

    #(37) Bootstrap
    "bootstrap": [{"LOWER": "bootstrap"}],
    "boot strap": [{"LOWER": "boot"}, {"LOWER": "strap"}],

    #(38) Django
    "django": [{"LOWER": "django"}],

    #(39) ElasticSearch
    "elasticsearch": [{"LOWER": "elasticsearch"}],
    "elastic search": [{"LOWER": "elastic"}, {"LOWER": "search"}],

    #(40) Entity Framework
    "entity framework": [{"LOWER": "entity"}, {"LOWER": "framework"}],

    #(41) Express.JS
    "express.js": [{"LOWER": "express.js"}],
    "expressjs": [{"LOWER": "expressjs"}],
    "express": [{"LOWER": "express"}],

    #(42) Flask
    "flask": [{"LOWER": "flask"}],

    #(43) Hibernate
    "hibernate": [{"LOWER": "hibernate"}],

    #(44) JavaServer Pages (JSP)
    "jsp": [{"LOWER": "jsp"}],
    "javaserver pages": [{"LOWER": "javaserver"}, {"LOWER": "pages"}],
    "java server pages": [{"LOWER": "java"}, {"LOWER": "server"}, {"LOWER": "pages"}],

    #(45) Java Database Connectivity (JDBC)
    "jdbc": [{"LOWER": "jdbc"}],
    "java database connectivity": [{"LOWER": "java"}, {"LOWER": "database"}, {"LOWER": "connectivity"}],

    #(46) JQuery
    "jquery": [{"LOWER": "jquery"}],

    #(47) JUnit
    "junit": [{"LOWER": "junit"}],

    #(48) OpenGL
    "opengl": [{"LOWER": "opengl"}],
    "open gl": [{"LOWER": "open"}, {"LOWER": "gl"}],

    #(49) React.JS
    "react": [{"LOWER": "react"}],
    "reactjs": [{"LOWER": "reactjs"}],
    "react.js": [{"LOWER": "react.js"}],

    #(50) React Native
    "react native": [{"LOWER": "react"}, {"LOWER": "native"}],

    #(51) Redux
    "redux": [{"LOWER": "redux"}],
    "reduxjs": [{"LOWER": "reduxjs"}],
    "redux.js": [{"LOWER": "redux.js"}],

    #(52) Selenium
    "selenium": [{"LOWER": "selenium"}],

    #(53) Java Servlets
    "servlets": [{"LOWER": "servlets"}, {"LOWER": "servlet"}],

    #(54) Spring Boot
    "spring boot": [{"LOWER": "spring"}, {"LOWER": "boot"}],

    #(55) Spring Framework
    "spring": [{"LOWER": "spring"}],

    #(56) Spring MVC
    "spring mvc": [{"LOWER": "spring"}, {"LOWER": "mvc"}],

    #(57) SQL Server Reporting Services (SSRS)
    "ssrs": [{"LOWER": "ssrs"}],
    "server reporting services": [{"LOWER": "server"}, {"LOWER": "reporting"}, {"LOWER": "services"}],

    #(58) Apache Struts
    "struts": [{"LOWER": "struts"}],

    #(59) TensorFlow
    "tensorflow": [{"LOWER": "tensorflow"}],
    "tensor flow": [{"LOWER": "tensor"}, {"LOWER": "flow"}],

    #(60) Unity
    "unity": [{"LOWER": "unity"}],
    "unity3D": [{"LOWER": "unity3D"}],

    #(61) Vue.JS
    "vue.js": [{"LOWER": "vue.js"}],
    "vuejs": [{"LOWER": "vuejs"}],
    "vue js": [{"LOWER": "vue"}, {"LOWER": "js"}],
    "vue .js": [{"LOWER": "vue"}, {"LOWER": ".js"}],

    #(62) Windows Communication Foundation (WCF)
    "wcf": [{"LOWER": "wcf"}],
    "windows communication foundation": [{"LOWER": "windows"}, {"LOWER": "communication"}, {"LOWER": "foundation"}],

    #(63) WordPress
    "wordpress": [{"LOWER": "wordpress"}],
    "word press": [{"LOWER": "word"}, {"LOWER": "press"}],

    #(64) Windows Presentation Foundation (WPF)
    "wpf": [{"LOWER": "wpf"}],
    "windows presentation foundation": [{"LOWER": "windows"}, {"LOWER": "presentation"}, {"LOWER": "foundation"}],

    #(65) SQL Server Integration Services (SSIS)
    "ssis": [{"LOWER": "ssis"}],
    "server integration services": [{"LOWER": "server"}, {"LOWER": "integration"}, {"LOWER": "services"}],

    #(66) DB2
    "db2": [{"LOWER": "db2"}],
    "db 2": [{"LOWER": "db"}, {"LOWER": "2"}],

    #(67) Microsoft SQL Server
    "sql server": [{"LOWER": "sql"}, {"LOWER": "server"}],
    "sqlserver": [{"LOWER": "sqlserver"}],

    #(68) MongoDB
    "mongo": [{"LOWER": "mongo"}],
    "mongodb": [{"LOWER": "mongodb"}],

    #(69) MySQL
    "mysql": [{"LOWER": "mysql"}],

    #(70) Oracle Database
    "oracle db": [{"LOWER": "oracle"}, {"LOWER": "db"}],
    "oracledb": [{"LOWER": "oracledb"}],
    "oracle database": [{"LOWER": "oracle"}, {"LOWER": "database"}],
    "oracle sql": [{"LOWER": "oracle"}, {"LOWER": "sql"}],

    #(71) PostgreSQL
    "postgresql": [{"LOWER": "postgresql"}],

    #(72) Redis
    "redis": [{"LOWER": "redis"}],

    #(73) SQLite
    "sqlite": [{"LOWER": "sqlite"}],

    #(74) MariaDB
    "mariadb": [{"LOWER": "mariadb"}],
    "maria db": [{"LOWER": "maria"}, {"LOWER": "db"}],
    "mariadatabase": [{"LOWER": "mariadatabase"}],

    #(75) IBM Informix
    "informix": [{"LOWER": "informix"}],

    #(76) SAP HANA
    "sap hana": [{"LOWER": "sap"}, {"LOWER": "hana"}],

    #(77) Apache Derby
    "apache derby": [{"LOWER": "apache"}, {"LOWER": "derby"}],

    #(78) Firebird
    "firebird": [{"LOWER": "firebird"}],

    #(79) Apache Cassandra
    "cassandra": [{"LOWER": "cassandra"}],

    #(80) CockroachDB
    "cockroachdb": [{"LOWER": "cockroachdb"}],
    "cockroach db": [{"LOWER": "cockroach"}, {"LOWER": "db"}],
    "cockroach database": [{"LOWER": "cockroach"}, {"LOWER": "database"}],

    #(81) Microsoft Access
    "microsoft access": [{"LOWER": "microsoft"}, {"LOWER": "access"}],
    "Access": [{"IS_TITLE": True, "LOWER": "access"}],

    #(82) Vertica
    "vertica": [{"LOWER": "vertica"}],

    #(83) Amazon Aurora
    "amazon aurora": [{"LOWER": "amazon"}, {"LOWER": "aurora"}],

    #(84) Apache CouchDB
    "couchdb": [{"LOWER": "couchdb"}],
    "couch db": [{"LOWER": "couch"}, {"LOWER": "db"}],
    "couch database": [{"LOWER": "couch"}, {"LOWER": "database"}],

    #(85) Apache HBase
    "hbase": [{"LOWER": "hbase"}],

    #(86) Couchbase
    "couchbase": [{"LOWER": "couchbase"}],

    #(87) ArangoDB
    "arangodb": [{"LOWER": "arangodb"}],
    "arango db": [{"LOWER": "arango"}, {"LOWER": "db"}],
    "arango database": [{"LOWER": "arango"}, {"LOWER": "database"}],

    #(88) Aerospike
    "aerospike": [{"LOWER": "aerospike"}],

    #(89) Riak
    "riak": [{"LOWER": "riak"}],

    #(90) MarkLogic
    "marklogic": [{"LOWER": "marklogic"}],

    #(91) Extensible Markup Language (XML)
    "xml": [{"LOWER": "xml"}],

    #(92) Google Cloud Datastore
    "google cloud datastore": [{"LOWER": "google"}, {"LOWER": "cloud"}, {"LOWER": "datastore"}],

    #(93) FaunaDB
    "faunadb": [{"LOWER": "faunadb"}],
    "fauna db": [{"LOWER": "fauna"}, {"LOWER": "db"}],
    "fauna database": [{"LOWER": "fauna"}, {"LOWER": "database"}],

    #(94) Apache Ignite
    "ignite": [{"LOWER": "ignite"}],

    #(95) GridGain
    "gridgain": [{"LOWER": "gridgain"}],

    #(96) VoltDB
    "voltdb": [{"LOWER": "voltdb"}],
    "volt db": [{"LOWER": "volt"}, {"LOWER": "db"}],
    "volt database": [{"LOWER": "volt"}, {"LOWER": "database"}],

    #(97) MemSQL
    "memsql": [{"LOWER": "memsql"}],

    #(98) Android Studio
    "android studio": [{"LOWER": "android"}, {"LOWER": "studio"}],
    "android sdk": [{"LOWER": "android"}, {"LOWER": "sdk"}],

    #(99) Ansible
    "ansible": [{"LOWER": "ansible"}],

    #(100) Ant
    "ant": [{"LOWER": "ant"}],

    #(101) Apache Kafka
    "kafka": [{"LOWER": "kafka"}],

    #(102) Rational ClearCase
    "clearcase": [{"LOWER": "clearcase"}, {"LOWER": "clear"}, {"LOWER": "case"}],
    "clear case": [{"LOWER": "clear"}, {"LOWER": "case"}],

    #(103) Confluence
    "confluence": [{"LOWER": "confluence"}],

    #(104) Crystal Reports
    "crystal reports": [{"LOWER": "crystal"}, {"LOWER": "reports"}],

    #(105) Customer Relationship Management (CRM)
    "customer relationship management": [{"LOWER": "customer"}, {"LOWER": "relationship"}, {"LOWER": "management"}],
    "crm": [{"LOWER": "crm"}],

    #(106) Docker
    "docker": [{"LOWER": "docker"}],

    #(107) E-commerce
    "ecommerce": [{"LOWER": "ecommerce"}],
    "e-commerce": [{"LOWER": "e"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "commerce"}],

    #(108) Eclipse IDE
    "eclipse": [{"LOWER": "eclipse"}],

    #(109) Enterprise Resource Planning (ERP)
    "enterprise resource planning": [{"LOWER": "enterprise"}, {"LOWER": "resource"}, {"LOWER": "planning"}],
    "erp": [{"LOWER": "erp"}],

    #(110) Firmware
    "firmware": [{"LOWER": "firmware"}],

    #(111) Git
    "git": [{"LOWER": "git"}],

    #(112) Hadoop
    "hadoop": [{"LOWER": "hadoop"}],

    #(113) Internet Information Services (IIS)
    "internet information services": [{"LOWER": "internet"}, {"LOWER": "information"}, {"LOWER": "services"}],
    "iis": [{"LOWER": "iis"}],

    #(114) IntelliJ IDEA
    "intellij": [{"LOWER": "intellij"}],

    #(115) iOS
    "ios": [{"LOWER": "ios"}],
    "iphone os": [{"LOWER": "iphone"}, {"LOWER": "os"}],

    #(116) JBoss
    "jboss": [{"LOWER": "jboss"}],

    #(117) Jenkins
    "jenkins": [{"LOWER": "jenkins"}],

    #(118) JIRA
    "jira": [{"LOWER": "jira"}],

    #(119) Kubernetes
    "kubernetes": [{"LOWER": "kubernetes"}],

    #(120) Linux
    "linux": [{"LOWER": "linux"}],
    "ubuntu": [{"LOWER": "ubuntu"}],
    "red hat": [{"LOWER": "red"}, {"LOWER": "hat"}],
    "redhat": [{"LOWER": "redhat"}],
    "centos": [{"LOWER": "centos"}],
    "debian": [{"LOWER": "debian"}],

    #(121) Maven
    "maven": [{"LOWER": "maven"}, {"LOWER": "mvn"}],

    #(122) Microsoft Azure
    "azure": [{"LOWER": "azure"}],

    #(123) Microsoft Excel
    "excel": [{"LOWER": "excel"}],

    #(124) Microsoft Office
    "microsoft office": [{"LOWER": "microsoft"}, {"LOWER": "office"}],
    "ms office": [{"LOWER": "ms"}, {"LOWER": "office"}],
    "ms office": [{"LOWER": "msoffice"}],

    #(125) Microsoft PowerPoint
    "powerpoint": [{"LOWER": "powerpoint"}],

    #(126) Microsoft Word
    "microsoft word": [{"LOWER": "microsoft"}, {"LOWER": "word"}],

    #(127) Microsoft Project
    "ms project": [{"LOWER": "ms"}, {"LOWER": "project"}],
    "msproject": [{"LOWER": "msproject"}],
    "microsoft project": [{"LOWER": "microsoft"}, {"LOWER": "project"}],

    #(128) Perforce
    "perforce": [{"LOWER": "perforce"}],

    #(129) Salesforce
    "salesforce": [{"LOWER": "salesforce"}],
    "salesforce.com": [{"LOWER": "salesforce"}, {"ORTH": "."}, {"LOWER": "com"}],

    #(130) Microsoft SharePoint
    "sharepoint": [{"LOWER": "sharepoint"}],

    #(131) Solaris
    "solaris": [{"LOWER": "solaris"}],

    #(132) Solidworks
    "solidworks": [{"LOWER": "solidworks"}],

    #(133) Tableau
    "tableau": [{"LOWER": "tableau"}],

    #(134) Team Foundation Server (TFS)
    "team foundation server": [{"LOWER": "team"}, {"LOWER": "foundation"}, {"LOWER": "server"}],
    "tfs": [{"LOWER": "tfs"}],

    #(135) Terraform
    "terraform": [{"LOWER": "terraform"}],

    #(136) Apache Tomcat
    "tomcat": [{"LOWER": "tomcat"}],

    #(137) Tortoise SVN
    "tortoise": [{"LOWER": "tortoise"}],

    #(138) Ubuntu
    "ubuntu": [{"LOWER": "ubuntu"}],

    #(139) Unix
    "unix": [{"LOWER": "unix"}],

    #(140) Microsoft Visio
    "visio": [{"LOWER": "visio"}],
    "msvisio": [{"LOWER": "msvisio"}],

    #(141) Microsoft Visual Studio
    "visual studio": [{"LOWER": "visual"}, {"LOWER": "studio"}],

    #(142) VMware
    "vmware": [{"LOWER": "vmware"}],

    #(143) WebLogic
    "weblogic": [{"LOWER": "weblogic"}],

    #(144) Microsoft Windows
    "microsoft windows": [{"LOWER": "microsoft"}, {"LOWER": "windows"}],
    "ms windows": [{"LOWER": "ms"}, {"LOWER": "windows"}],
    "windows 7": [{"LOWER": "windows"}, {"LOWER": "7"}],

    #(145) Microsoft Windows Server
    "windows server": [{"LOWER": "windows"}, {"LOWER": "server"}],

    #(146) Xcode
    "xcode": [{"LOWER": "xcode"}],
    "x code": [{"LOWER": "x"}, {"LOWER": "code"}],

    #(147) VSCode
    "vscode": [{"LOWER": "vscode"}],
    "vs code": [{"LOWER": "vs"}, {"LOWER": "code"}],

    #(148) Agile Methodologies
    "agile": [{"LOWER": "agile"}],

    #(149) Algorithms
    "algorithm": [{"LOWER": "algorithm"}],
    "algorithms": [{"LOWER": "algorithms"}],

    #(150) Customer Service
    "customer service": [{"LOWER": "customer"}, {"LOWER": "service"}],

    #(151) Strategic Partnerships
    "strategic partnerships": [{"LOWER": "strategic"}, {"LOWER": "partnerships"}],
    "strategic partnership": [{"LOWER": "strategic"}, {"LOWER": "partnership"}],

    #(152) Amazon Web Services (AWS)
    "aws": [{"LOWER": "aws"}],
    "amazon web services": [{"LOWER": "amazon"}, {"LOWER": "web"}, {"LOWER": "services"}],

    #(153) Android Development
    "android development": [{"LOWER": "android"}, {"LOWER": "development"}],

    #(154) API Development
    "api development": [{"LOWER": "api"}, {"LOWER": "development"}],

    #(155) Application Development
    "application development": [{"LOWER": "application"}, {"LOWER": "development"}],

    #(156) Software Architecture
    "software architecture": [{"LOWER": "software"}, {"LOWER": "architecture"}],
    "solution architecture": [{"LOWER": "solution"}, {"LOWER": "architecture"}],
    "system architecture": [{"LOWER": "system"}, {"LOWER": "architecture"}],
    "application architecture": [{"LOWER": "application"}, {"LOWER": "architecture"}],
    "architectural design": [{"LOWER": "architectural"}, {"LOWER": "design"}],
    "architecture design": [{"LOWER": "architecture"}, {"LOWER": "design"}],

    #(157) Artificial Intelligence (AI)
    "ai": [{"LOWER": "ai"}],
    "artificial intelligence": [{"LOWER": "artificial"}, {"LOWER": "intelligence"}],

    #(158) Critical Thinking
    "critical thinking": [{"LOWER": "critical"}, {"LOWER": "thinking"}],

    #(159) Azure
    "azure": [{"LOWER": "azure"}],

    #(160) BackEnd Development
    "backend": [{"LOWER": "backend"}],
    "back-end": [{"LOWER": "back"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "end"}],

    # (161) Big Data
    "bigdata": [{"LOWER": "bigdata"}],
    "big data": [{"LOWER": "big"}, {"LOWER": "data"}],

    # (162) Business Analysis
    "business analysis": [{"LOWER": "business"}, {"LOWER": "analysis"}],

    # (163) Business Intelligence
    "business intelligence": [{"LOWER": "business"}, {"LOWER": "intelligence"}],
    "bi": [{"LOWER": "bi"}],

    # (164) Cloud Computing
    "cloud computing": [{"LOWER": "cloud"}, {"LOWER": "computing"}],

    # (165) Continuous Integration and Continuous Delivery (CI/CD)
    "continuous integration": [{"LOWER": "continuous"}, {"LOWER": "integration"}],
    "continuous delivery": [{"LOWER": "continuous"}, {"LOWER": "delivery"}],
    "ci/cd": [{"LOWER": "ci"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "cd"}],

    # (166) Data Mining
    "data mining": [{"LOWER": "data"}, {"LOWER": "mining"}],

    # (167) Data Modeling
    "data modeling": [{"LOWER": "data"}, {"LOWER": "modeling"}],

    # (168) Data Science
    "data science": [{"LOWER": "data"}, {"LOWER": "science"}],

    # (169) Data Structures
    "data structures": [{"LOWER": "data"}, {"LOWER": "structures"}],
    "data structure": [{"LOWER": "data"}, {"LOWER": "structure"}],

    # (170) Data Visualization
    "data visualization": [{"LOWER": "data"}, {"LOWER": "visualization"}],

    # (171) Database Administration
    "database administration": [{"LOWER": "database"}, {"LOWER": "administration"}],

    # (172) Database Design
    "database design": [{"LOWER": "database"}, {"LOWER": "design"}],

    # (173) Database Modeling
    "database modeling": [{"LOWER": "database"}, {"LOWER": "modeling"}],

    # (174) Debugging
    "debugging": [{"LOWER": "debugging"}],

    # (175) Deep Learning
    "deep learning": [{"LOWER": "deep"}, {"LOWER": "learning"}],

    # (176) Design Patterns
    "design patterns": [{"LOWER": "design"}, {"LOWER": "patterns"}],
    "design pattern": [{"LOWER": "design"}, {"LOWER": "pattern"}],

    # (177) DevOps
    "devops": [{"LOWER": "devops"}],

    # (178) Disaster Recovery
    "disaster recovery": [{"LOWER": "disaster"}, {"LOWER": "recovery"}],

    # (179) Distributed Systems
    "distributed systems": [{"LOWER": "distributed"}, {"LOWER": "systems"}],
    "distributed system": [{"LOWER": "distributed"}, {"LOWER": "system"}],

    # (180) Engineering/Development Management
    "engineering management": [{"LOWER": "engineering"}, {"LOWER": "management"}],
    "development management": [{"LOWER": "development"}, {"LOWER": "management"}],

    #(181) Enterprise Architecture
    "enterprise architecture": [{"LOWER": "enterprise"}, {"LOWER": "architecture"}],

    #(182) Extract Transform Load (ETL)
    "etl": [{"LOWER": "etl"}],

    #(183) FrontEnd Development
    "frontend": [{"LOWER": "frontend"}],
    "front-end": [{"LOWER": "front"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "end"}],

    #(184) FullStack Development
    "fullstack": [{"LOWER": "fullstack"}],
    "full-stack": [{"LOWER": "full"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "stack"}],

    #(185) Game Design
    "game design": [{"LOWER": "game"}, {"LOWER": "design"}],

    #(186) Game Development
    "game development": [{"LOWER": "game"}, {"LOWER": "development"}],

    #(187) Google Cloud Platform (GCP)
    "google cloud": [{"LOWER": "google"}, {"LOWER": "cloud"}],
    "gcp": [{"LOWER": "gcp"}],

    #(188) Information Security
    "information security": [{"LOWER": "information"}, {"LOWER": "security"}],

    #(189) iOS Development
    "ios development": [{"LOWER": "ios"}, {"LOWER": "development"}],

    #(190) IT Management
    "it management": [{"LOWER": "it"}, {"LOWER": "management"}],
    "it service management": [{"LOWER": "it"}, {"LOWER": "service"}, {"LOWER": "management"}],
    "information technology management": [{"LOWER": "information"}, {"LOWER": "technology"}, {"LOWER": "management"}],

    #(191) Information Technology Infrastructure Library (ITIL)
    "information technology infrastructure library": [{"LOWER": "information"}, {"LOWER": "technology"}, {"LOWER": "infrastructure"}, {"LOWER": "library"}],
    "itil": [{"LOWER": "itil"}],

    #(192) Machine Learning
    "machine learning": [{"LOWER": "machine"}, {"LOWER": "learning"}],

    #(193) Microservices
    "microservices": [{"LOWER": "microservices"}],
    "microservice": [{"LOWER": "microservice"}],

    #(194) Mobile Development
    "mobile development": [{"LOWER": "mobile"}, {"LOWER": "development"}],
    "mobile application development": [{"LOWER": "mobile"}, {"LOWER": "application"}, {"LOWER": "development"}],
    "mobile applications development": [{"LOWER": "mobile"}, {"LOWER": "applications"}, {"LOWER": "development"}],

    #(195) Multithreading
    "multithreading": [{"LOWER": "multithreading"}],
    "multi-threading": [{"LOWER": "multi"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "threading"}],

    #(196) Network Administration
    "networking administration": [{"LOWER": "networking"}, {"LOWER": "administration"}],

    #(197) NoSQL Databases
    "nosql": [{"LOWER": "nosql"}],

    #(198) Object-Oriented Programming (OOP)
    "object-oriented": [{"LOWER": "object"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "oriented"}],
    "oop": [{"LOWER": "oop"}],

    #(199) Project Management Professional (PMP)
    "project management professional": [{"LOWER": "project"}, {"LOWER": "management"}, {"LOWER": "professional"}],
    "pmp": [{"LOWER": "pmp"}],

    #(200) Software Development
    "macos": [{"LOWER": "macos"}],
    "mac os:": [{"LOWER": "mac"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "os"}],
    "os x": [{"LOWER": "os"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "x"}],

    #(201) Product Management
    "product management": [{"LOWER": "product"}, {"LOWER": "management"}],
    "program management": [{"LOWER": "program"}, {"LOWER": "management"}],

    #(202) Project Management
    "project management": [{"LOWER": "project"}, {"LOWER": "management"}],

    #(203) Project Planning
    "project planning": [{"LOWER": "project"}, {"LOWER": "planning"}],

    #(204) Relational Databases
    "relational databases": [{"LOWER": "relational"}, {"LOWER": "databases"}],

    #(205) REST API WebServices
    "restful": [{"LOWER": "restful"}],
    "rest": [{"LOWER": "rest"}],
    "representational state transfer": [{"LOWER": "representational"}, {"LOWER": "state"}, {"LOWER": "transfer"}],
    "application programming interfaces": [{"LOWER": "application"}, {"LOWER": "programming"}, {"LOWER": "interfaces"}],

    #(206) Requirements Analysis
    "requirements analysis": [{"LOWER": "requirements"}, {"LOWER": "analysis"}],
    "requirement analysis": [{"LOWER": "requirement"}, {"LOWER": "analysis"}],
    "business requirements": [{"LOWER": "business"}, {"LOWER": "requirements"}],
    "business requirement": [{"LOWER": "business"}, {"LOWER": "requirement"}],
    
    #(207) Requirements Gathering
    "requirements gathering": [{"LOWER": "requirements"}, {"LOWER": "gathering"}],
    "requirement gathering": [{"LOWER": "requirement"}, {"LOWER": "gathering"}],

    #(208) Robotics
    "robotics": [{"LOWER": "robotics"}],
    "robotic": [{"LOWER": "robotic"}],

    #(209) Software as a Service (SASS)
    "sofware as a service": [{"LOWER": "sofware"}, {"LOWER": "as"}, {"LOWER": "a"}, {"LOWER": "service"}],
    "sass": [{"LOWER": "sass"}],

    #(210) Scalability
    "scalability": [{"LOWER": "scalability"}],

    #(211) Scrum
    "scrum": [{"LOWER": "scrum"}],

    #(212) Software Development Lifecycle (SDLC)
    "software development lifecycle": [{"LOWER": "sofware"}, {"LOWER": "development"}, {"LOWER": "lifecycle"}],
    "software development life cycle": [{"LOWER": "sofware"}, {"LOWER": "development"}, {"LOWER": "life"}, {"LOWER": "cycle"}],
    "software lifecycle": [{"LOWER": "sofware"}, {"LOWER": "lifecycle"}],
    "software life cycle": [{"LOWER": "sofware"}, {"LOWER": "life"}, {"LOWER": "cycle"}],
    "sdlc": [{"LOWER": "sdlc"}],
    "application lifecycle": [{"LOWER": "application"}, {"LOWER": "lifecycle"}],
    "application life cycle": [{"LOWER": "application"}, {"LOWER": "life"}, {"LOWER": "cycle"}],
    "alm": [{"LOWER": "alm"}],

    #(213) Search Engine Optimization (SEO)
    "search engine optimization": [{"LOWER": "search"}, {"LOWER": "engine"}, {"LOWER": "optimization"}],
    "seo": [{"LOWER": "seo"}],

    #(214) Service Oriented Architecture (SOA)
    "service oriented architecture": [{"LOWER": "service"}, {"LOWER": "oriented"}, {"LOWER": "architecture"}],
    "soa": [{"LOWER": "soa"}],

    #(215) Simple Object Access Protocol (SOAP)
    "soap": [{"LOWER": "soap"}],

    #(216) Software Design
    "software design": [{"LOWER": "software"}, {"LOWER": "design"}],

    #(217) Application Security
    "application security": [{"LOWER": "application"}, {"LOWER": "security"}],
    "application vulnerabilities": [{"LOWER": "application"}, {"LOWER": "vulnerabilities"}],
    "application vulnerability": [{"LOWER": "application"}, {"LOWER": "vulnerability"}],

    #(218) Software Documentation
    "software documentation": [{"LOWER": "software"}, {"LOWER": "documentation"}],

    #(219) Software Engineering
    "software engineering": [{"LOWER": "software"}, {"LOWER": "engineering"}],
    "system engineering": [{"LOWER": "system"}, {"LOWER": "engineering"}],
    "systems engineering": [{"LOWER": "systems"}, {"LOWER": "engineering"}],

    #(220) Software Project Management
    "software project management": [{"LOWER": "software"}, {"LOWER": "project"}, {"LOWER": "management"}],

    #(221) Software Quality Assurance
    "software quality assurance": [{"LOWER": "software"}, {"LOWER": "quality"}, {"LOWER": "assurance"}],

    #(222) Software Testing
    "software testing": [{"LOWER": "software"}, {"LOWER": "testing"}],
    "regression testing": [{"LOWER": "regression"}, {"LOWER": "testing"}],
    "test cases": [{"LOWER": "test"}, {"LOWER": "cases"}],
    "test automation": [{"LOWER": "test"}, {"LOWER": "automation"}],
    "test driven development": [{"LOWER": "test"}, {"LOWER": "driven"}, {"LOWER": "development"}],
    "test planning": [{"LOWER": "test"}, {"LOWER": "planning"}],
    "unit testing": [{"LOWER": "unit"}, {"LOWER": "testing"}],
    "unit tests": [{"LOWER": "unit"}, {"LOWER": "tests"}],
    "unit test": [{"LOWER": "unit"}, {"LOWER": "test"}],
    "user acceptance testing": [{"LOWER": "user"}, {"LOWER": "acceptance"}, {"LOWER": "testing"}],
    "manual testing": [{"LOWER": "manual"}, {"LOWER": "testing"}],
    "manual test": [{"LOWER": "manual"}, {"LOWER": "test"}],
    "api testing": [{"LOWER": "api"}, {"LOWER": "testing"}],
    "black box testing": [{"LOWER": "black"}, {"LOWER": "box"}, {"LOWER": "testing"}],
    "blackbox testing": [{"LOWER": "blackbox"}, {"LOWER": "testing"}],
    "functional testing": [{"LOWER": "functional"}, {"LOWER": "testing"}],

    #(223) Team Management
    "team management": [{"LOWER": "team"}, {"LOWER": "management"}],

    #(224) Technical Leadership
    "technical leadership": [{"LOWER": "technical"}, {"LOWER": "leadership"}],

    #(225) Technical Support
    "technical support": [{"LOWER": "technical"}, {"LOWER": "support"}],

    #(226) Technical Writing
    "technical writing": [{"LOWER": "technical"}, {"LOWER": "writing"}],

    #(227) Web Development
    "web development": [{"LOWER": "web"}, {"LOWER": "development"}],
    "web application development": [{"LOWER": "web"}, {"LOWER": "application"}, {"LOWER": "development"}],
    "web design": [{"LOWER": "web"}, {"LOWER": "design"}],

    #(228) Web Services
    "web services": [{"LOWER": "web"}, {"LOWER": "services"}],

    #(229) User Experience (UI) and User Interface (UX) Design
    "user experience": [{"LOWER": "user"}, {"LOWER": "experience"}],
    "user interface": [{"LOWER": "user"}, {"LOWER": "interface"}],
    "ux design": [{"LOWER": "ux"}, {"LOWER": "design"}],
    "ui design": [{"LOWER": "ui"}, {"LOWER": "design"}],
    "ui/ux": [{"LOWER": "ui"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "ux"}],
    "ux/ui": [{"LOWER": "ux"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "ui"}],

    #(230) Unified Modeling Language (UML)
    "unified modeling language": [{"LOWER": "unified"}, {"LOWER": "modeling"}, {"LOWER": "language"}],
    "uml": [{"LOWER": "uml"}],

    #(231) eXtensible Stylesheet Language for Transformation (XSLT)
    "xslt": [{"LOWER": "xslt"}],

    #(232) Lamport TeX (LaTeX)
    "latex": [{"LOWER": "latex"}],

    #(233) Automation	
    "automation": [{"LOWER": "automation"}],

    #(234) Computer Hardware
    "hardware": [{"LOWER": "hardware"}],

    #(235) Cyber Security
    "cyber security": [{"LOWER": "cyber"}, {"LOWER": "security"}],
    "cybersecurity": [{"LOWER": "cybersecurity"}],

    #(236) Data Analysis
    "data analysis": [{"LOWER": "data"}, {"LOWER": "analysis"}],

    #(237) Entrepreneurship
    "entrepreneurship": [{"LOWER": "entrepreneurship"}],

    #(238) Google Analytics
    "google analytics": [{"LOWER": "google"}, {"LOWER": "analytics"}], 

    #(239) Graphic Design
    "graphic design": [{"LOWER": "graphic"}, {"LOWER": "design"}],

    #(240) Leadership
    "leadership": [{"LOWER": "leadership"}],

    #(241) Mentoring and Training
    "mentoring": [{"LOWER": "mentoring"}],
    "teaching": [{"LOWER": "teaching"}],
    "coaching": [{"LOWER": "coaching"}],
    "training": [{"LOWER": "training"}],

    #(242) Problem Solving
    "problem solving": [{"LOWER": "problem"}, {"LOWER": "solving"}],

    #(243) Process Improvement
    "process improvement": [{"LOWER": "process"}, {"LOWER": "improvement"}],

    #(244) Public Speaking
    "public speaking": [{"LOWER": "public"}, {"LOWER": "speaking"}],

    #(245) Quality Assurance
    "quality assurance": [{"LOWER": "quality"}, {"LOWER": "assurance"}],

    #(246) Research
    "research": [{"LOWER": "research"}],

    #(247) Statistics
    "statistics": [{"LOWER": "statistics"}],

    #(248) System Administration
    "system administration": [{"LOWER": "system"}, {"LOWER": "administration"}],
    "systems adminitration": [{"LOWER": "systems"}, {"LOWER": "administration"}],
    
    #(249) Systems Analysis
    "systems analysis": [{"LOWER": "systems"}, {"LOWER": "analysis"}],
    "system analysis": [{"LOWER": "system"}, {"LOWER": "analysis"}],
    "analysis services": [{"LOWER": "analysis"}, {"LOWER": "services"}],
    
    #(250) Team Building
    "team building": [{"LOWER": "team"}, {"LOWER": "building"}],

    #(251) Team Player
    "teamwork": [{"LOWER": "teamwork"}],
    "team work": [{"LOWER": "team"}, {"LOWER": "work"}],
    "team player": [{"LOWER": "team"}, {"LOWER": "player"}],
    "collaboration": [{"LOWER": "collaboration"}],
    "collaborative": [{"LOWER": "collaborative"}],
    
    #(252) Telecommunications
    "telecommunications": [{"LOWER": "telecommunications"}],
    "telecommunication": [{"LOWER": "telecommunication"}],
    
    #(253) Time Management
    "time management": [{"LOWER": "time"}, {"LOWER": "management"}],

    #(254) .NET Framework
    "dotnet framework":  [{"LOWER": "dotnet"}, {"LOWER": "framework"}],
    ".net framework": [{"LOWER": ".net"}, {"LOWER": "framework"}],
    "dot net framework": [{"LOWER": "dot"}, {"LOWER": "net"}, {"LOWER": "framework"}],

    #(255) JavaScript Object Notation (JSON)
    "javaScript object notation": [{"LOWER": "javaScript"}, {"LOWER": "object"}, {"LOWER": "notation"}],
    "json": [{"LOWER": "json"}],

    #(256) Troubleshooting
    "troubleshooting": [{"LOWER": "troubleshooting"}],

    #(257) Strategic Planning
    "strategic planning": [{"LOWER": "strategic"}, {"LOWER": "planning"}],

    #(258) Enterprise Software
    "enterprise software": [{"LOWER": "enterprise"}, {"LOWER": "software"}],

    #(259) Communication
    "communication": [{"LOWER": "communication"}],

    #(260) Apache Subversion (SVN)
    "apache subversion": [{"LOWER": "apache"}, {"LOWER": "subversion"}],
    "svn": [{"LOWER": "svn"}],

    #(261) GitHub
    "github": [{"LOWER": "github"}],
    
    #(262) GitLab
    "gitlab": [{"LOWER": "gitlab"}],

    #(263) Embedded Systems
    "embedded systems": [{"LOWER": "embedded"}, {"LOWER": "systems"}],
    "embedded system": [{"LOWER": "embedded"}, {"LOWER": "system"}],
    "embedded software": [{"LOWER": "embedded"}, {"LOWER": "software"}],

    #(264) Application Programming Interfaces (API)
    "application programming interfaces": [{"LOWER": "application"}, {"LOWER": "programming"}, {"LOWER": "interfaces"}],
    "api": [{"LOWER": "api"}],

    #(265) Recruiting
    "recruiting": [{"LOWER": "recruiting"}],

    #(266) Shell Scripting
    "shell scripting": [{"LOWER": "shell"}, {"LOWER": "scripting"}],
    "shell script": [{"LOWER": "shell"}, {"LOWER": "script"}],

    #(267) Cross-functional Team Leadership
    "cross functional team leadership": [{"LOWER": "cross"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "functional"}, {"LOWER": "team"}, {"LOWER": "leadership"}],

    #(268) Business Development
    "business development": [{"LOWER": "business"}, {"LOWER": "development"}],

    #(269) Computer Science Fundamentals
    "computer science": [{"LOWER": "computer"}, {"LOWER": "science"}],

    #(270) Test Driven Development (TDD)
    "test driven development": [{"LOWER": "test"}, {"LOWER": "driven"}, {"LOWER": "development"}],
    "tdd": [{"LOWER": "tdd"}],

    #(271) Marketing
    "marketing": [{"LOWER": "marketing"}],

    #(272) Data Warehousing
    "data warehousing": [{"LOWER": "data"}, {"LOWER": "warehousing"}],

    #(273) Vendor Management
    "vendor management": [{"LOWER": "vendor"}, {"LOWER": "management"}],

    #(274) Consulting
    "consulting": [{"LOWER": "consulting"}],

    #(275) Business Strategy
    "business strategy": [{"LOWER": "business"}, {"LOWER": "strategy"}],

    #(276) Microsoft Active Directory
    "active directory": [{"LOWER": "active"}, {"LOWER": "directory"}],

    #(277) Transmission Control Protocol/Internet Protocol (TCP/IP)
    "transmission control protocol": [{"LOWER": "transmission"}, {"LOWER": "control"}, {"LOWER": "protocol"}],
    "internet protocol": [{"LOWER": "internet"}, {"LOWER": "protocol"}],
    "tcp/ip": [{"LOWER": "tcp"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "ip"}],

    #(278) Startup Environment
    "startup": [{"LOWER": "startup"}],
    "startups": [{"LOWER": "startups"}],
    "start-ups": [{"LOWER": "start"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "ups"}],
    "start-up": [{"LOWER": "start"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "up"}],

    #(279) Analytical Skills
    "analytical skills": [{"LOWER": "analytical"}, {"LOWER": "skills"}],
    "analytical skill": [{"LOWER": "analytical"}, {"LOWER": "skill"}],

    #(280) Information Technology Strategy
    "information technology strategy": [{"LOWER": "information"}, {"LOWER": "technology"}, {"LOWER": "strategy"}],
    "it strategy": [{"LOWER": "it"}, {"LOWER": "strategy"}],

    #(281) Change Management
    "change management": [{"LOWER": "change"}, {"LOWER": "management"}],

    #(282) Virtualization
    "virtualization": [{"LOWER": "virtualization"}],

    #(283) Account Management
    "account management": [{"LOWER": "account"}, {"LOWER": "management"}],

    #(284) AutoCAD
    "autocad": [{"LOWER": "autocad"}],

    #(285) English
    "english": [{"LOWER": "english"}],

    #(286) Network Security
    "network security": [{"LOWER": "network"}, {"LOWER": "security"}],

    #(287) Marketing Strategy
    "marketing strategy": [{"LOWER": "marketing"}, {"LOWER": "strategy"}],

    #(288) Manufacturing Processes
    "manufacturing": [{"LOWER": "manufacturing"}],

    #(289) Adobe Photoshop
    "photoshop": [{"LOWER": "photoshop"}],

    #(290) Operations Management
    "operations management": [{"LOWER": "operations"}, {"LOWER": "management"}],

    #(291) .NET Core
    "dotnet core": [{"LOWER": "dotnet"}, {"LOWER": "core"}],
    ".net core": [{"LOWER": ".net"}, {"LOWER": "core"}],
    "dot net core": [{"LOWER": "dot"}, {"LOWER": "net"}, {"LOWER": "core"}],

    #(292) Sales Management
    "sales management": [{"LOWER": "sales"}, {"LOWER": "management"}],

    #(293) Data Center Operations
    "data center": [{"LOWER": "data"}, {"LOWER": "center"}],

    #(294) Event Planning
    "event planning": [{"LOWER": "event"}, {"LOWER": "planning"}],

    #(295) Social Media Marketing
    "social media marketing": [{"LOWER": "social"}, {"LOWER": "media"}, {"LOWER": "marketing"}],

    #(296) Adobe Creative Suite
    "adobe creative suite": [{"LOWER": "adobe"}, {"LOWER": "creative"}, {"LOWER": "suite"}],

    #(297) Data Analytics
    "data analytics": [{"LOWER": "data"}, {"LOWER": "analytics"}],

    #(298) Risk Management
    "risk management": [{"LOWER": "risk"}, {"LOWER": "management"}],

    #(299) Simulations
    "simulations": [{"LOWER": "simulations"}],

    #(300) Contract Negotiation
    "contract negotiation": [{"LOWER": "contract"}, {"LOWER": "negotiation"}],

    #(301) Device Drivers Engineering
    "device drivers": [{"LOWER": "device"}, {"LOWER": "drivers"}],
    "device driver": [{"LOWER": "device"}, {"LOWER": "driver"}],

    #(302) Computer Vision
    "computer vision": [{"LOWER": "computer"}, {"LOWER": "vision"}],

    #(303) Amazon Elastic Compute Cloud (Amazon EC2)
    "amazon ec2": [{"LOWER": "amazon"}, {"LOWER": "ec2"}],
    "aws ec2": [{"LOWER": "aws"}, {"LOWER": "ec2"}],
    "elastic compute cloud": [{"LOWER": "elastic"}, {"LOWER": "compute"}, {"LOWER": "cloud"}],

    #(304) AWS Lambda
    "aws lambda": [{"LOWER": "aws"}, {"LOWER": "lambda"}],
    "amazon lambda": [{"LOWER": "amazon"}, {"LOWER": "lambda"}],

    #(305) AWS Batch
    "aws batch": [{"LOWER": "aws"}, {"LOWER": "batch"}],
    "amazon batch": [{"LOWER": "amazon"}, {"LOWER": "batch"}],

    #(306) Amazon Lightsail
    "amazon lightsail": [{"LOWER": "amazon"}, {"LOWER": "lightsail"}],
    "aws lightsail": [{"LOWER": "aws"}, {"LOWER": "lightsail"}],
    "lightsail": [{"LOWER": "lightsail"}],

    #(307) AWS Elastic Beanstalk
    "aws elastic beanstalk": [{"LOWER": "aws"}, {"LOWER": "elastic"}, {"LOWER": "beanstalk"}],
    "amazon elastic beanstalk": [{"LOWER": "amazon"}, {"LOWER": "elastic"}, {"LOWER": "beanstalk"}],
    "elastic beanstalk": [{"LOWER": "elastic"}, {"LOWER": "beanstalk"}],

    #(308) AWS Fargate
    "aws fargate": [{"LOWER": "aws"}, {"LOWER": "fargate"}],
    "amazon fargate": [{"LOWER": "amazon"}, {"LOWER": "fargate"}],
    "fargate": [{"LOWER": "fargate"}],

    #(309) AWS Outposts
    "aws outposts": [{"LOWER": "aws"}, {"LOWER": "outposts"}],
    "amazon outposts": [{"LOWER": "amazon"}, {"LOWER": "outposts"}],
    "outposts": [{"LOWER": "outposts"}],

    #(310) AWS Serverless Application Repository
    "aws serverless application repository": [{"LOWER": "aws"}, {"LOWER": "serverless"}, {"LOWER": "application"}, {"LOWER": "repository"}],
    "amazon serverless application repository": [{"LOWER": "amazon"}, {"LOWER": "serverless"}, {"LOWER": "application"}, {"LOWER": "repository"}],
    "serverless application repository": [{"LOWER": "serverless"}, {"LOWER": "application"}, {"LOWER": "repository"}],

    #(311) AWS Snow Family
    "aws snow": [{"LOWER": "aws"}, {"LOWER": "snow"}],
    "amazon snow": [{"LOWER": "amazon"}, {"LOWER": "snow"}],

    #(312) Amazon Simple Storage Service (Amazon S3)
    "amazon s3": [{"LOWER": "amazon"}, {"LOWER": "s3"}],
    "aws s3": [{"LOWER": "aws"}, {"LOWER": "s3"}],
    "simple storage service": [{"LOWER": "simple"}, {"LOWER": "storage"}, {"LOWER": "service"}],

    #(313) Amazon Elastic Block Store (Amazon EBS)
    "amazon ebs": [{"LOWER": "amazon"}, {"LOWER": "ebs"}],
    "aws ebs": [{"LOWER": "aws"}, {"LOWER": "ebs"}],
    "elastic block store": [{"LOWER": "elastic"}, {"LOWER": "block"}, {"LOWER": "store"}],

    #(314) Amazon Elastic File System (Amazon EFS)
    "amazon efs": [{"LOWER": "amazon"}, {"LOWER": "efs"}],
    "aws efs": [{"LOWER": "aws"}, {"LOWER": "efs"}],
    "elastic file system": [{"LOWER": "elastic"}, {"LOWER": "file"}, {"LOWER": "system"}],

    #(315) Amazon File Systems (Amazon FSx)
    "amazon fsx": [{"LOWER": "amazon"}, {"LOWER": "fsx"}],
    "aws fsx": [{"LOWER": "aws"}, {"LOWER": "fsx"}],
    "amazon file systems": [{"LOWER": "amazon"}, {"LOWER": "file"}, {"LOWER": "systems"}],
    "aws file systems": [{"LOWER": "aws"}, {"LOWER": "file"}, {"LOWER": "systems"}],

    #(316) Amazon S3 Glacier
    "amazon glacier": [{"LOWER": "amazon"}, {"LOWER": "glacier"}],
    "aws glacier": [{"LOWER": "aws"}, {"LOWER": "glacier"}],
    "s3 glacier": [{"LOWER": "s3"}, {"LOWER": "glacier"}],

    #(317) AWS Storage Gateway
    "aws storage gateway": [{"LOWER": "aws"}, {"LOWER": "storage"}, {"LOWER": "gateway"}],
    "amazon storage gateway": [{"LOWER": "amazon"}, {"LOWER": "storage"}, {"LOWER": "gateway"}],

    #(318) AWS Backup
    "aws backup": [{"LOWER": "aws"}, {"LOWER": "backup"}],
    "amazon backup": [{"LOWER": "amazon"}, {"LOWER": "backup"}],

    #(319) Amazon Relational Database Service (Amazon RDS)
    "amazon rds": [{"LOWER": "amazon"}, {"LOWER": "rds"}],
    "aws rds": [{"LOWER": "aws"}, {"LOWER": "rds"}],
    "relational database service": [{"LOWER": "relational"}, {"LOWER": "database"}, {"LOWER": "service"}],

    #(320) Amazon DynamoDB
    "dynamodb": [{"LOWER": "dynamodb"}],
    "dynamo db": [{"LOWER": "dynamo"}, {"LOWER": "db"}],
    "dynamo database": [{"LOWER": "dynamo"}, {"LOWER": "database"}],

    #(321) Amazon ElastiCache
    "elasticache": [{"LOWER": "elasticache"}],

    #(322) Amazon Neptune
    "amazon neptune": [{"LOWER": "amazon"}, {"LOWER": "neptune"}],
    "aws neptune": [{"LOWER": "aws"}, {"LOWER": "neptune"}],

    #(323) Amazon Redshift
    "redshift": [{"LOWER": "redshift"}],

    #(324) AWS Database Migration Service (Amazon DMS)
    "database migration service": [{"LOWER": "database"}, {"LOWER": "migration"}, {"LOWER": "service"}],
    "aws dms": [{"LOWER": "aws"}, {"LOWER": "dms"}],
    "amazon dms": [{"LOWER": "amazon"}, {"LOWER": "dms"}],

    #(325) Amazon DocumentDB
    "documentdb": [{"LOWER": "documentdb"}],
    "document db": [{"LOWER": "document"}, {"LOWER": "db"}],

    #(326) Amazon Timestream
    "amazon timestream": [{"LOWER": "amazon"}, {"LOWER": "timestream"}],
    "aws timestream": [{"LOWER": "aws"}, {"LOWER": "timestream"}],

    #(327) Amazon Virtual Private Cloud (Amazon VPC)
    "amazon vpc": [{"LOWER": "amazon"}, {"LOWER": "vpc"}],
    "aws vpc": [{"LOWER": "aws"}, {"LOWER": "vpc"}],
    "virtual private cloud": [{"LOWER": "virtual"}, {"LOWER": "private"}, {"LOWER": "cloud"}],

    #(328) Amazon Route 53
    "route 53": [{"LOWER": "route"}, {"LOWER": "53"}],

    #(329) Amazon API Gateway
    "amazon api gateway": [{"LOWER": "amazon"}, {"LOWER": "api"}, {"LOWER": "gateway"}],
    "aws api gateway": [{"LOWER": "aws"}, {"LOWER": "api"}, {"LOWER": "gateway"}],

    #(330) AWS Direct Connect
    "aws direct connect": [{"LOWER": "aws"}, {"LOWER": "direct"}, {"LOWER": "connect"}],
    "amazon direct connect": [{"LOWER": "amazon"}, {"LOWER": "direct"}, {"LOWER": "connect"}],

    #(331) AWS App Mesh
    "app mesh": [{"LOWER": "app"}, {"LOWER": "mesh"}],

    #(332) Amazon CloudFront
    "cloudfront": [{"LOWER": "cloudfront"}],

    #(333) AWS Global Accelerator
    "aws global accelerator": [{"LOWER": "aws"}, {"LOWER": "global"}, {"LOWER": "accelerator"}],
    "amazon global accelerator": [{"LOWER": "amazon"}, {"LOWER": "global"}, {"LOWER": "accelerator"}],

    #(334) AWS Transit Gateway
    "aws transit gateway": [{"LOWER": "aws"}, {"LOWER": "transit"}, {"LOWER": "gateway"}],
    "amazon transit gateway": [{"LOWER": "amazon"}, {"LOWER": "transit"}, {"LOWER": "gateway"}],

    #(335) AWS PrivateLink
    "aws privatelink": [{"LOWER": "aws"}, {"LOWER": "privatelink"}],
    "amazon privatelink": [{"LOWER": "amazon"}, {"LOWER": "privatelink"}],

    #(336) Amazon Elastic Load Balancing (Amazon ELB)
    "amazon elb": [{"LOWER": "amazon"}, {"LOWER": "elb"}],
    "aws elb": [{"LOWER": "aws"}, {"LOWER": "elb"}],
    "elastic load balancing": [{"LOWER": "elastic"}, {"LOWER": "load"}, {"LOWER": "balancing"}],

    #(337) AWS Identity and Access Management (AWS IAM)
    "aws iam": [{"LOWER": "aws"}, {"LOWER": "iam"}],
    "amazon iam": [{"LOWER": "amazon"}, {"LOWER": "iam"}],
    "aws identity and access management": [{"LOWER": "aws"}, {"LOWER": "identity"}, {"LOWER": "and"}, {"LOWER": "access"}, {"LOWER": "management"}],
    "amazon identity and access management": [{"LOWER": "amazon"}, {"LOWER": "identity"}, {"LOWER": "and"}, {"LOWER": "access"}, {"LOWER": "management"}],

    #(338) AWS Organizations
    "aws organizations": [{"LOWER": "aws"}, {"LOWER": "organizations"}],
    "amazon organizations": [{"LOWER": "amazon"}, {"LOWER": "organizations"}],

    #(339) AWS Certificate Manager (ACM)
    "aws certificate manager": [{"LOWER": "aws"}, {"LOWER": "certificate"}, {"LOWER": "manager"}],
    "amazon certificate manager": [{"LOWER": "amazon"}, {"LOWER": "certificate"}, {"LOWER": "manager"}],
    "aws acm": [{"LOWER": "aws"}, {"LOWER": "acm"}],
    "amazon acm": [{"LOWER": "amazon"}, {"LOWER": "acm"}],

    #(340) AWS AWS Secrets Manager
    "aws secrets manager": [{"LOWER": "aws"}, {"LOWER": "secrets"}, {"LOWER": "manager"}],
    "amazon secrets manager": [{"LOWER": "amazon"}, {"LOWER": "secrets"}, {"LOWER": "manager"}],

    #(341) Amazon Web Application Firewall (AWS WAF)
    "aws waf": [{"LOWER": "aws"}, {"LOWER": "waf"}],
    "amazon waf": [{"LOWER": "amazon"}, {"LOWER": "waf"}],
    "aws web application firewall": [{"LOWER": "aws"}, {"LOWER": "web"}, {"LOWER": "application"}, {"LOWER": "firewall"}],
    "amazon web application firewall": [{"LOWER": "amazon"}, {"LOWER": "web"}, {"LOWER": "application"}, {"LOWER": "firewall"}],

    #(342) Amazon GuardDuty
    "amazon guardduty": [{"LOWER": "amazon"}, {"LOWER": "guardduty"}],
    "aws guardduty": [{"LOWER": "aws"}, {"LOWER": "guardduty"}],

    #(343) Amazon Macie
    "amazon macie": [{"LOWER": "amazon"}, {"LOWER": "macie"}],
    "aws macie": [{"LOWER": "aws"}, {"LOWER": "macie"}],

    #(344) AWS Shield
    "aws shield": [{"LOWER": "aws"}, {"LOWER": "shield"}],
    "amazon shield": [{"LOWER": "amazon"}, {"LOWER": "shield"}],

    #(345) AWS Artifact
    "aws artifact": [{"LOWER": "aws"}, {"LOWER": "artifact"}],
    "amazon artifact": [{"LOWER": "amazon"}, {"LOWER": "artifact"}],

    #(346) AWS Single Sign-On (Amazon SSO)
    "aws sso": [{"LOWER": "aws"}, {"LOWER": "sso"}],
    "amazon sso": [{"LOWER": "amazon"}, {"LOWER": "sso"}],
    "aws single sign-on": [{"LOWER": "aws"}, {"LOWER": "single"}, {"LOWER": "sign"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "on"}],
    "amazon single sign-on": [{"LOWER": "amazon"}, {"LOWER": "single"}, {"LOWER": "sign"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "on"}],

    #(347) Amazon Athena
    "amazon athena": [{"LOWER": "amazon"}, {"LOWER": "athena"}],
    "aws athena": [{"LOWER": "aws"}, {"LOWER": "athena"}],

    #(348) Amazon Elastic MapReduce (Amazon EMR)
    "amazon emr": [{"LOWER": "amazon"}, {"LOWER": "emr"}],
    "aws emr": [{"LOWER": "aws"}, {"LOWER": "emr"}],
    "amazon elastic mapreduce": [{"LOWER": "amazon"}, {"LOWER": "elastic"}, {"LOWER": "mapreduce"}],
    "aws elastic mapreduce": [{"LOWER": "aws"}, {"LOWER": "elastic"}, {"LOWER": "mapreduce"}],
    "amazon elastic map reduce": [{"LOWER": "amazon"}, {"LOWER": "elastic"}, {"LOWER": "map"}, {"LOWER": "reduce"}],
    "aws elastic map reduce": [{"LOWER": "aws"}, {"LOWER": "elastic"}, {"LOWER": "map"}, {"LOWER": "reduce"}],

    #(349) Amazon QuickSight
    "quicksight": [{"LOWER": "quicksight"}],
    "quick sight": [{"LOWER": "quick"}, {"LOWER": "sight"}],

    #(350) Amazon Kinesis
    "amazon kinesis": [{"LOWER": "amazon"}, {"LOWER": "kinesis"}],
    "aws kinesis": [{"LOWER": "aws"}, {"LOWER": "kinesis"}],

    #(351) AWS Data Pipeline
    "aws data pipeline": [{"LOWER": "aws"}, {"LOWER": "data"}, {"LOWER": "pipeline"}],
    "amazon data pipeline": [{"LOWER": "amazon"}, {"LOWER": "data"}, {"LOWER": "pipeline"}],

    #(352) AWS Glue
    "aws glue": [{"LOWER": "aws"}, {"LOWER": "glue"}],
    "amazon glue": [{"LOWER": "amazon"}, {"LOWER": "glue"}],

    #(353) AWS Lake Formation
    "aws lake formation": [{"LOWER": "aws"}, {"LOWER": "lake"}, {"LOWER": "formation"}],
    "amazon lake formation": [{"LOWER": "amazon"}, {"LOWER": "lake"}, {"LOWER": "formation"}],

    #(354) Amazon Managed Streaming for Apache Kafka (Amazon MSK)
    "amazon msk": [{"LOWER": "amazon"}, {"LOWER": "msk"}],
    "aws msk": [{"LOWER": "aws"}, {"LOWER": "msk"}],
    "managed streaming for apache kafka": [{"LOWER": "managed"}, {"LOWER": "streaming"}, {"LOWER": "for"}, {"LOWER": "apache"}, {"LOWER": "kafka"}],

    #(355) AWS Database Migration Service (Amazon DMS)
    "aws dms": [{"LOWER": "aws"}, {"LOWER": "dms"}],
    "amazon dms": [{"LOWER": "amazon"}, {"LOWER": "dms"}],
    "aws database migration service": [{"LOWER": "database"}, {"LOWER": "migration"}, {"LOWER": "service"}],
    "amazon database migration service": [{"LOWER": "amazon"}, {"LOWER": "database"}, {"LOWER": "migration"}, {"LOWER": "service"}],

    #(356) Amazon SageMaker
    "sagemaker": [{"LOWER": "sagemaker"}],

    #(357) Amazon Comprehend
    "amazon comprehend": [{"LOWER": "amazon"}, {"LOWER": "comprehend"}],
    "aws comprehend": [{"LOWER": "aws"}, {"LOWER": "comprehend"}],

    #(358) Amazon Lex
    "amazon lex": [{"LOWER": "amazon"}, {"LOWER": "lex"}],
    "aws lex": [{"LOWER": "aws"}, {"LOWER": "lex"}],

    #(359) Amazon Polly
    "amazon polly": [{"LOWER": "amazon"}, {"LOWER": "polly"}],
    "aws polly": [{"LOWER": "aws"}, {"LOWER": "polly"}],

    #(360) Amazon Rekognition
    "amazon rekognition": [{"LOWER": "amazon"}, {"LOWER": "rekognition"}],
    "aws rekognition": [{"LOWER": "aws"}, {"LOWER": "rekognition"}],

    #(361) Amazon TextTract
    "amazon texttract": [{"LOWER": "amazon"}, {"LOWER": "texttract"}],
    "aws texttract": [{"LOWER": "aws"}, {"LOWER": "texttract"}],

    #(362) Amazon Translate
    "amazon translate": [{"LOWER": "amazon"}, {"LOWER": "translate"}],
    "aws translate": [{"LOWER": "aws"}, {"LOWER": "translate"}],

    #(363) Amazon Transcribe
    "amazon transcribe": [{"LOWER": "amazon"}, {"LOWER": "transcribe"}],
    "aws transcribe": [{"LOWER": "aws"}, {"LOWER": "transcribe"}],

    #(364) AWS DeepRacer
    "aws deepracer": [{"LOWER": "aws"}, {"LOWER": "deepracer"}],
    "amazon deepracer": [{"LOWER": "amazon"}, {"LOWER": "deepracer"}],

    #(365) AWS DeepLens
    "aws deeplens": [{"LOWER": "aws"}, {"LOWER": "deeplens"}],
    "amazon deeplens": [{"LOWER": "amazon"}, {"LOWER": "deeplens"}],

    #(366) AWS DeepComposer
    "aws deepcomposer": [{"LOWER": "aws"}, {"LOWER": "deepcomposer"}],
    "amazon deepcomposer": [{"LOWER": "amazon"}, {"LOWER": "deepcomposer"}],

    #(367) Amazon Simple Queue Service (Amazon SQS)
    "amazon sqs": [{"LOWER": "amazon"}, {"LOWER": "sqs"}],
    "aws sqs": [{"LOWER": "aws"}, {"LOWER": "sqs"}],
    "amazon simple queue service": [{"LOWER": "amazon"}, {"LOWER": "simple"}, {"LOWER": "queue"}, {"LOWER": "service"}],
    "aws simple queue service": [{"LOWER": "aws"}, {"LOWER": "simple"}, {"LOWER": "queue"}, {"LOWER": "service"}],

    #(368) Amazon Simple Notification Service (Amazon SNS)
    "amazon sns": [{"LOWER": "amazon"}, {"LOWER": "sns"}],
    "aws sns": [{"LOWER": "aws"}, {"LOWER": "sns"}],
    "amazon simple notification service": [{"LOWER": "amazon"}, {"LOWER": "simple"}, {"LOWER": "notification"}, {"LOWER": "service"}],
    "aws simple notification service": [{"LOWER": "aws"}, {"LOWER": "simple"}, {"LOWER": "notification"}, {"LOWER": "service"}],

    #(369) Amazon EventBridge
    "eventbridge": [{"LOWER": "eventbridge"}],

    #(370) Amazon AppFlow
    "amazon appflow": [{"LOWER": "amazon"}, {"LOWER": "appflow"}],
    "aws appflow": [{"LOWER": "aws"}, {"LOWER": "appflow"}],

    #(371) AWS Step Functions
    "aws step functions": [{"LOWER": "aws"}, {"LOWER": "step"}, {"LOWER": "functions"}],
    "amazon step functions": [{"LOWER": "amazon"}, {"LOWER": "step"}, {"LOWER": "functions"}],

    #(372) AWS Simple Workflow Service (Amazon SWF)
    "aws swf": [{"LOWER": "aws"}, {"LOWER": "swf"}],
    "amazon swf": [{"LOWER": "amazon"}, {"LOWER": "swf"}],
    "aws simple workflow service": [{"LOWER": "aws"}, {"LOWER": "simple"}, {"LOWER": "workflow"}, {"LOWER": "service"}],
    "amazon simple workflow service": [{"LOWER": "amazon"}, {"LOWER": "simple"}, {"LOWER": "workflow"}, {"LOWER": "service"}],

    #(373) Amazon CloudWatch
    "cloudwatch": [{"LOWER": "cloudwatch"}],

    #(374) AWS Auto Scaling
    "aws auto scaling": [{"LOWER": "aws"}, {"LOWER": "auto"}, {"LOWER": "scaling"}],
    "amazon auto scaling": [{"LOWER": "amazon"}, {"LOWER": "auto"}, {"LOWER": "scaling"}],

    #(375) AWS CloudFormation
    "cloudformation": [{"LOWER": "cloudformation"}],

    #(376) AWS CloudTrail
    "cloudtrail": [{"LOWER": "cloudtrail"}],

    #(377) AWS Config
    "aws config": [{"LOWER": "aws"}, {"LOWER": "config"}],
    "amazon config": [{"LOWER": "amazon"}, {"LOWER": "config"}],

    #(378) AWS OpsWorks
    "opsworks": [{"LOWER": "opsworks"}],

    #(379) AWS Service Catalog
    "aws service catalog": [{"LOWER": "aws"}, {"LOWER": "service"}, {"LOWER": "catalog"}],
    "amazon service catalog": [{"LOWER": "amazon"}, {"LOWER": "service"}, {"LOWER": "catalog"}],

    #(380) AWS Trusted Advisor
    "aws trusted advisor": [{"LOWER": "aws"}, {"LOWER": "trusted"}, {"LOWER": "advisor"}],
    "amazon trusted advisor": [{"LOWER": "amazon"}, {"LOWER": "trusted"}, {"LOWER": "advisor"}],

    #(381) AWS Well-Architected Tool
    "aws well-architected tool": [{"LOWER": "aws"}, {"LOWER": "well"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "architected"}, {"LOWER": "tool"}],
    "amazon well-architected tool": [{"LOWER": "amazon"}, {"LOWER": "well"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "architected"}, {"LOWER": "tool"}],

    #(382) AWS Control Tower
    "aws control tower": [{"LOWER": "aws"}, {"LOWER": "control"}, {"LOWER": "tower"}],
    "amazon control tower": [{"LOWER": "amazon"}, {"LOWER": "control"}, {"LOWER": "tower"}],

    #(383) AWS IoT Core
    "aws iot core": [{"LOWER": "aws"}, {"LOWER": "iot"}, {"LOWER": "core"}],
    "amazon iot core": [{"LOWER": "amazon"}, {"LOWER": "iot"}, {"LOWER": "core"}],

    #(384) AWS IoT Device Management
    "aws iot device management": [{"LOWER": "aws"}, {"LOWER": "iot"}, {"LOWER": "device"}, {"LOWER": "management"}],
    "amazon iot device management": [{"LOWER": "amazon"}, {"LOWER": "iot"}, {"LOWER": "device"}, {"LOWER": "management"}],

    #(385) AWS IoT Analytics
    "aws iot analytics": [{"LOWER": "aws"}, {"LOWER": "iot"}, {"LOWER": "analytics"}],
    "amazon iot analytics": [{"LOWER": "amazon"}, {"LOWER": "iot"}, {"LOWER": "analytics"}],

    #(386) AWS IoT Greengrass
    "aws iot greengrass": [{"LOWER": "aws"}, {"LOWER": "iot"}, {"LOWER": "greengrass"}],
    "amazon iot greengrass": [{"LOWER": "amazon"}, {"LOWER": "iot"}, {"LOWER": "greengrass"}],

    #(387) Waterfall Methodologies
    "waterfall": [{"LOWER": "waterfall"}],

    #(388) Product Marketing
    "product marketing": [{"LOWER": "product"}, {"LOWER": "marketing"}],

    #(389) Customer Satisfaction
    "customer satisfaction": [{"LOWER": "customer"}, {"LOWER": "satisfaction"}],

    #(390) Continuous Improvement
    "continuous improvement": [{"LOWER": "continuous"}, {"LOWER": "improvement"}],

    #(391) Electrical Engineering
    "electrical engineering": [{"LOWER": "electrical"}, {"LOWER": "engineering"}],

    #(392) Pre-sales Operations
    "pre-sales": [{"LOWER": "pre"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "sales"}],

    #(393) Cloud Security
    "cloud security": [{"LOWER": "cloud"}, {"LOWER": "security"}],

    #(394) Data Security
    "data security": [{"LOWER": "data"}, {"LOWER": "security"}],

    #(395) Identity and Access Management (IAM)
    "identity and access management": [{"LOWER": "identity"}, {"LOWER": "and"}, {"LOWER": "access"}, {"LOWER": "management"}],
    "iam": [{"LOWER": "iam"}],

    #(396) Incident Response
    "incident response": [{"LOWER": "incident"}, {"LOWER": "response"}],

    #(397) Security Architecture
    "security architecture": [{"LOWER": "security"}, {"LOWER": "architecture"}],

    #(398) Vulnerability Management
    "vulnerability management": [{"LOWER": "vulnerability"}, {"LOWER": "management"}],

    #(399) Penetration Testing
    "penetration testing": [{"LOWER": "penetration"}, {"LOWER": "testing"}],
    "penetration test": [{"LOWER": "penetration"}, {"LOWER": "test"}],

    #(400) Security Awareness and Training
    "security awareness": [{"LOWER": "security"}, {"LOWER": "awareness"}],
    "security training": [{"LOWER": "security"}, {"LOWER": "training"}],
    "security advocate": [{"LOWER": "security"}, {"LOWER": "advocate"}],

    #(401) Cryptography
    "cryptography": [{"LOWER": "cryptography"}],

    #(402) Security Operations
    "security operations": [{"LOWER": "security"}, {"LOWER": "operations"}],

    #(403) Security Governance and Compliance
    "security governance": [{"LOWER": "security"}, {"LOWER": "governance"}],
    "security compliance": [{"LOWER": "security"}, {"LOWER": "compliance"}],

    #(404) Mobile Security
    "mobile security": [{"LOWER": "mobile"}, {"LOWER": "security"}],

    #(405) Wireless Security
    "wireless security": [{"LOWER": "wireless"}, {"LOWER": "security"}],

    #(406) Social Engineering
    "social engineering": [{"LOWER": "social"}, {"LOWER": "engineering"}],

    #(407) Cisco Technologies
    "cisco technologies": [{"LOWER": "cisco"}, {"LOWER": "technologies"}],
    "cisco technology": [{"LOWER": "cisco"}, {"LOWER": "technology"}],

    #(408) Microsoft Exchange
    "microsoft exchange": [{"LOWER": "microsoft"}, {"LOWER": "exchange"}],
    "ms exchange": [{"LOWER": "ms"}, {"LOWER": "exchange"}],

    #(409) Adobe Illustrator
    "adobe illustrator": [{"LOWER": "adobe"}, {"LOWER": "illustrator"}],

    #(410) Digital Marketing
    "digital marketing": [{"LOWER": "digital"}, {"LOWER": "marketing"}],

    #(411) Mathematics
    "mathematics": [{"LOWER": "mathematics"}],

    #(412) Image Processing
    "image processing": [{"LOWER": "image"}, {"LOWER": "processing"}],

    #(413) XHTML
    "xhtml": [{"LOWER": "xhtml"}],

    #(414) Financial Analysis
    "financial analysis": [{"LOWER": "financial"}, {"LOWER": "analysis"}],

    #(415) Six Sigma
    "six sigma": [{"LOWER": "six"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "sigma"}],
    "6 sigma": [{"LOWER": "6"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "sigma"}],

    #(416) Arduino
    "arduino": [{"LOWER": "arduino"}],

    #(417) Firebase
    "firebase": [{"LOWER": "firebase"}],

    #(418) Software Installation
    "software installation": [{"LOWER": "software"}, {"LOWER": "installation"}],

    #(419) Security Clearance
    "security clearance": [{"LOWER": "security"}, {"LOWER": "clearance"}],

    #(420) Forecasting
    "forecasting": [{"LOWER": "forecasting"}],

    #(421) Labview
    "labview": [{"LOWER": "labview"}],

    #(422) Laravel
    "laravel": [{"LOWER": "laravel"}],

    #(423) Voice over Internet Protocol (VoIP)
    "voice over internet protocol": [{"LOWER": "voice"}, {"LOWER": "over"}, {"LOWER": "internet"}, {"LOWER": "protocol"}],
    "voip": [{"LOWER": "voip"}],

    #(424) Microsoft Power BI
    "power bi": [{"LOWER": "power"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "bi"}],

    #(425) IBM WebSphere Application Server
    "websphere": [{"LOWER": "websphere"}],

    #(426) Sales Operations
    "sales operations": [{"LOWER": "sales"}, {"LOWER": "operations"}],

    #(427) Data Migration
    "data migration": [{"LOWER": "data"}, {"LOWER": "migration"}],

    #(428) Solution Selling
    "solution selling": [{"LOWER": "solution"}, {"LOWER": "selling"}],

    #(429) Microsoft Silverlight
    "silverlight": [{"LOWER": "silverlight"}],

    #(430) Performance Tuning
    "performance tuning": [{"LOWER": "performance"}, {"LOWER": "tuning"}],

    #(431) Microcontrollers
    "microcontrollers": [{"LOWER": "microcontrollers"}],
    "microcontroller": [{"LOWER": "microcontroller"}],

    #(432) Management Consulting
    "management consulting": [{"LOWER": "management"}, {"LOWER": "consulting"}],

    #(433) Competitive Analysis
    "competitive analysis": [{"LOWER": "competitive"}, {"LOWER": "analysis"}],

    #(434) Market Research
    "market research": [{"LOWER": "market"}, {"LOWER": "research"}],

    #(435) ActionScript
    "actionscript": [{"LOWER": "actionscript"}],
    "action-script": [{"LOWER": "action"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "script"}],

    #(436) Groovy
    "groovy": [{"LOWER": "groovy"}],

    #(437) Windows Forms
    "windows forms": [{"LOWER": "windows"}, {"LOWER": "forms"}],
    "winforms": [{"LOWER": "winforms"}],

    #(438) Event Management
    "event management": [{"LOWER": "event"}, {"LOWER": "management"}],

    #(439) Healthcare
    "healthcare": [{"LOWER": "healthcare"}],

    #(440) Microsoft Visual Basic Scripting Edition (VBScript)
    "vbscript": [{"LOWER": "vbscript"}],
    "vb-script": [{"LOWER": "vb"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "script"}],
    "visual basic script": [{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": "script"}],
    "visual basic scripting": [{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": "scripting"}],

    #(441) Budget Planning
    "budget planning": [{"LOWER": "budget"}, {"LOWER": "planning"}],
    "budgeting": [{"LOWER": "budgeting"}],

    #(442) Lean Manufacturing
    "lean manufacturing": [{"LOWER": "lean"}, {"LOWER": "manufacturing"}],

    #(443) NumPy
    "numpy": [{"LOWER": "numpy"}],

    #(444) Real-Time Operating System (RTOS)
    "real-time operating system": [{"LOWER": "real"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "time"}, {"LOWER": "operating"}, {"LOWER": "system"}],
    "rtos": [{"LOWER": "rtos"}],

    #(445) Bitbucket
    "bitbucket": [{"LOWER": "bitbucket"}],

    #(446) Assembly Language
    "assembly": [{"LOWER": "assembly"}],

    #(447) Content Management Systems (CMS)
    "content management system": [{"LOWER": "content"}, {"LOWER": "management"}, {"LOWER": "system"}],
    "cms": [{"LOWER": "cms"}],

    #(448) COBOL
    "cobol": [{"LOWER": "cobol"}],

    #(449) IT Infrastructure
    "infrastructure": [{"LOWER": "infrastructure"}],

    #(450) Java Persistence API (JPA)
    "jpa": [{"LOWER": "jpa"}],
    "java persistence api": [{"LOWER": "java"}, {"LOWER": "persistence"}, {"LOWER": "api"}],

    #(451) Business Planning
    "business planning": [{"LOWER": "business"}, {"LOWER": "planning"}],

    #(452) Retail
    "retail": [{"LOWER": "retail"}],

    #(453) Qt (toolkit)
    "qt": [{"IS_TITLE": True, "LOWER": "qt"}],

    #(454) Drupal
    "drupal": [{"LOWER": "drupal"}],

    #(455) Finance Understanding
    "finance": [{"LOWER": "finance"}],

    #(456) Open-source software (OSS)
    "open-source": [{"LOWER": "open"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "source"}],
    "opensource": [{"LOWER": "opensource"}],

}
