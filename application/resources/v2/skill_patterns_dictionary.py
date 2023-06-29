skill_patterns = {
    "Java": [
        ("java", '[{"LOWER": {"IN": ["java", "jee", "j2ee"]} }]'),
    ],
    "Python": [
        ("python", '[{"LOWER": "python"}]'),
    ],
    "CSharp": [
        ("csharp", '[{"LOWER": "csharp"}]'),
        ("c sharp", '[{"LOWER": "c"}, {"LOWER": "sharp"}]'),
        ("c#", '[{"LOWER": "c"},{"TEXT": {"REGEX": "#"} }]'),
    ],
    "Objective-C": [ 
        ("objective-c", '[{"LOWER": "objective"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "c"}]'),
        ("objectivec", '[{"LOWER": {"IN": ["objectivec", "objective.c"]} }]'),
    ],
    "Golang": [
        ("go", '[{"IS_TITLE": true, "LOWER": "go"}]'),
        ("golang", '[{"LOWER": "golang"}]'),
        ("go programming", '[{"LOWER": "go"}, {"LOWER": {"IN": ["programming", "language"]} }]'),
        ("go (programming", '[{"LOWER": "go"}, {"LOWER": "("}, , {"LOWER": {"IN": ["programming", "language"]} }]'),
    ],
    "Kotlin": [
        ("kotlin", '[{"LOWER": "kotlin"}]'),
    ],
    "Rust": [
        ("rust", '[{"LOWER": "rust"}]'),
    ],
    "VB.Net": [ 
        ("vb.net", '[{"LOWER": {"IN": "vb.net", "vbnet"} }]'),
        ("visual basic .net", '[{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": {"IN": ["net", ".net", "dotnet"]} }]'),
        ("vb .net", '[{"LOWER": {"IN": "vb", "visual"} }, {"LOWER": {"IN": ["net", ".net", "dotnet"]} }]'),
    ],
    "ASP.Net": [ 
        ("asp.net", '[{"LOWER": {"IN": "asp.net", "aspnet"} }]'),
        ("asp .net", '[{"LOWER": "asp"}, {"LOWER": {"IN": ["net", ".net", "dotnet"]} }]'),
    ],
    "Bash": [
        ("bash", '[{"LOWER": "bash"}]'),
    ],
    "Visual Basic 6": [
        ("visual basic 6", '[{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": "6"}]'),
        ("vb6", '[{"LOWER": "vb6"}]'),
        ("vb 6", '[{"LOWER": "vb"}, {"LOWER": "6"}]'),
    ],
    "C": [
        ("c" , '[{"LOWER": {"NOT_IN": ["objective", "-", "quite", "exactly", "Embedded"]} }, {"LOWER": "c"}, {"LOWER": {"NOT_IN": ["sharp", "+", "#", ".net", "dotnet", "dot", "-", "shell", "*"]} }]'),
    ],
    "C++": [
        ("c++", '[{"LOWER": "c++"}]'),
        ("c ++", '[{"LOWER": "c"}, {"LOWER": "++"}]'),
        ("c + +", '[{"LOWER": "c"}, {"LOWER": "+"}, {"LOWER": "+"}]'),
    ],
    "CSS": [
        ("css", '[{"LOWER": {"IN": ["css", "css3]} }]'),
    ],
    "GraphQL": [
        ("graphql", '[{"LOWER": "graphql"}]'),
    ],
    "HTML": [
        ("html", '[{"LOWER": {"IN": ["html", "html5"]} }]'),
    ],
    "Javascript": [
        ("javascript", '[{"LOWER": "javascript"}]'),
        ("java script", '[{"LOWER": "java"}, {"LOWER": "script"}]'),
    ],
    "Language Integrated Query (LINQ)": [
        ("linq", '[{"LOWER": "linq"}]'),
        ("language integrated query", '[{"LOWER": "language"}, {"LOWER": "integrated"}, {"LOWER": "query"}]'),
    ],
    "Matlab": [
        ("matlab", '[{"LOWER": "matlab"}]'),
        ("mat lab", '[{"LOWER": "mat"}, {"LOWER": "lab"}]'),
    ],
    "NodeJS": [
        ("nodejs", '[{"LOWER": {"IN": ["nodejs", "node.js"]} }]'),
        ("node js", '[{"LOWER": "node"}, {"LOWER": {"IN": [".js", "js"]} }]'),
    ],
    "Perl": [
        ("Perl", '[{"LOWER": "perl"}]'),
    ],
    "PHP": [
        ("php", '[{"LOWER": "php"}]'),
    ],
    "Ruby": [
        ("ruby", '[{"LOWER": "ruby"}]'),
        ("rubyonrails", '[{"LOWER": "rubyonrails"}]'),
    ],
    "Scala": [
        ("scala", '[{"LOWER": "scala"}]'),
    ],
    "Shell": [
        ("shell", '[{"LOWER": {"NOT_IN": ["power"]} }, {"LOWER": "shell"}]'),
    ],
    "Powershell": [
        ("powershell", '[{"LOWER": "powershell"}]'),
        ("power shell", '[{"LOWER": "power"}, {"LOWER": "shell"}]'),
    ],
    "Swift": [
        ("swift", '[{"LOWER": "swift"}]'),
    ],
    "R": [
        ("r" , '[{"LOWER": "r"}, {"LOWER": {"NOT_IN": ["+"]} }]'),
    ],
    "Typescript": [
        ("typescript", '[{"LOWER": "typescript"}]'),
        ("type script", '[{"LOWER": "type"}, {"LOWER": "script"}]'),
    ],
    "SQL": [
        ("sql", '[{"LOWER": "sql"}]'),
        ("tsql", '[{"LOWER": "tsql"}]'),
        ("plsql", '[{"LOWER": "plsql"}]'),
    ],
    "ADO.NET": [
        ("ado.net", '[{"LOWER": {"IN": ["ado.net", "adonet"]} }]'),
        ("ado net", '[{"LOWER": "ado"}, {"LOWER": {"IN": [".net", "net", "dotnet"]} }]'),
    ],
    "Asynchronous JavaScript And XML (AJAX)": [
        ("asynchronous javaScript and xml", '[{"LOWER": "asynchronous"}, {"LOWER": "javascript"}, {"LOWER": "and"}, {"LOWER": "xml"}]'),
        ("ajax", '[{"LOWER": "ajax"}]'),
    ],
    "Angular": [
        ("angular", '[{"LOWER": "angular"}]'),
        ("angular2", '[{"LOWER": "angular2"}]'),
    ],
    "Angular.JS": [
        ("angularjs", '[{"LOWER": {"IN": ["angularjs", "angular.js"]} }]'),
    ],
    "Apache Spark": [
        ("spark", '[{"LOWER": "spark"}]'),
    ],
    "Bootstrap": [
        ("bootstrap", '[{"LOWER": "bootstrap"}]'),
        ("boot strap", '[{"LOWER": "boot"}, {"LOWER": "strap"}]'),
    ],
    "Django": [
        ("django", '[{"LOWER": "django"}]'),
    ],
    "ElasticSearch": [
        ("elasticsearch", '[{"LOWER": "elasticsearch"}]'),
        ("elastic search", '[{"LOWER": "elastic"}, {"LOWER": "search"}]'),
    ],
    "Entity Framework": [
        ("entity framework", '[{"LOWER": "entity"}, {"LOWER": "framework"}]'),
    ],
    "Express.JS": [
        ("express.js", '[{"LOWER": {"IN": ["express.js", "expressjs", "express"]} }]'),
    ],
    "Flask": [
        ("flask", '[{"LOWER": "flask"}]'),
    ],
    "Hibernate": [
        ("hibernate", '[{"LOWER": "hibernate"}]'),
    ],
    "JavaServer Pages (JSP)": [
        ("jsp", '[{"LOWER": "jsp"}]'),
        ("javaserver pages", '[{"LOWER": "javaserver"}, {"LOWER": "pages"}]'),
        ("java server pages", '[{"LOWER": "java"}, {"LOWER": "server"}, {"LOWER": "pages"}]'),
    ],
    "Java Database Connectivity (JDBC)": [
        ("jdbc", '[{"LOWER": "jdbc"}]'),
        ("java database connectivity", '[{"LOWER": "java"}, {"LOWER": "database"}, {"LOWER": "connectivity"}]'),
    ],
    "JQuery": [
        ("jquery", '[{"LOWER": "jquery"}]'),
    ],
    "JUnit": [
        ("junit", '[{"LOWER": "junit"}]'),
    ],
    "OpenGL": [
        ("opengl", '[{"LOWER": "opengl"}]'),
        ("open gl", '[{"LOWER": "open"}, {"LOWER": "gl"}]'),
    ],
    "React.JS": [
        ("react", '[{"LOWER": {"IN": ["react", "reactjs", "react.js"]} }]'),
    ],
    "React Native": [
        ("react native", '[{"LOWER": "react"}, {"LOWER": "native"}]'),
    ],
    "Redux": [
        ("redux", '[{"LOWER": {"IN": ["redux", "reduxjs", "redux.js"]} }]'),
    ],
    "Selenium": [
        ("selenium", '[{"LOWER": "selenium"}]'),
    ],
    "Java Servlets": [
        ("servlets", '[{"LOWER": "servlets"}, {"LOWER": "servlet"}]'),
    ],
    "Spring Boot": [
        ("spring boot", '[{"LOWER": "spring"}, {"LOWER": "boot"}]'),
    ],
    "Spring Framework": [
        ("spring", '[{"LOWER": "spring"}]'),
    ],
    "Spring MVC": [
        ("spring mvc", '[{"LOWER": "spring"}, {"LOWER": "mvc"}]'),
    ],
    "SQL Server Reporting Services (SSRS)": [
        ("ssrs", '[{"LOWER": "ssrs"}]'),
        ("server reporting services", '[{"LOWER": "server"}, {"LOWER": "reporting"}, {"LOWER": "services"}]'),
    ],
    "Apache Struts": [
        ("struts", '[{"LOWER": "struts"}]'),
    ],
    "TensorFlow": [
        ("tensorflow", '[{"LOWER": "tensorflow"}]'),
        ("tensor flow", '[{"LOWER": "tensor"}, {"LOWER": "flow"}]'),
    ],
    "Unity": [
        ("unity", '[{"LOWER": "unity"}]'),
        ("unity3D", '[{"LOWER": "unity3D"}]'),
    ],
    "Vue.JS": [
        ("vue.js", '[{"LOWER": {"IN": ["vue.js", "vuejs"]} }]'),
        ("vue js", '[{"LOWER": "vue"}, {"LOWER": {"IN": [".js", "js"]} }]'),
    ],
    "Windows Communication Foundation (WCF)": [
        ("wcf", '[{"LOWER": "wcf"}]'),
        ("windows communication foundation", '[{"LOWER": "windows"}, {"LOWER": "communication"}, {"LOWER": "foundation"}]'),
    ],
    "WordPress": [
        ("wordpress", '[{"LOWER": "wordpress"}]'),
        ("word press", '[{"LOWER": "word"}, {"LOWER": "press"}]'),
    ],
    "Windows Presentation Foundation (WPF)": [
        ("wpf", '[{"LOWER": "wpf"}]'),
        ("windows presentation foundation", '[{"LOWER": "windows"}, {"LOWER": "presentation"}, {"LOWER": "foundation"}]'),
    ],
    "SQL Server Integration Services (SSIS)": [
        ("ssis", '[{"LOWER": "ssis"}]'),
        ("server integration services", '[{"LOWER": "server"}, {"LOWER": "integration"}, {"LOWER": "services"}]'),
    ],
    "DB2": [
        ("db2", '[{"LOWER": "db2"}]'),
        ("db 2", '[{"LOWER": "db"}, {"LOWER": "2"}]'),
    ],
    "Microsoft SQL Server": [
        ("sql server", '[{"LOWER": "sql"}, {"LOWER": "server"}]'),
        ("sqlserver", '[{"LOWER": "sqlserver"}]'),
    ],
    "MongoDB": [
        ("mongo", '[{"LOWER": "mongo"}]'),
        ("mongodb", '[{"LOWER": "mongodb"}]'),
    ],
    "MySQL": [
        ("mysql", '[{"LOWER": "mysql"}]'),
    ],
    "Oracle Database": [
        ("oracle db", '[{"LOWER": "oracle"}, {"LOWER": {"IN": ["db", "database", "sql"]} }]'),
        ("oracledb", '[{"LOWER": "oracledb"}]'),
    ],
    "PostgreSQL": [
        ("postgresql", '[{"LOWER": "postgresql"}]'),
    ],
    "Redis": [
        ("redis", '[{"LOWER": "redis"}]'),
    ],
    "SQLite": [
        ("sqlite", '[{"LOWER": "sqlite"}]'),
    ],
    "MariaDB": [
        ("mariadb", '[{"LOWER": {"IN": ["mariadb", "mariadatabase"]} }]'),
        ("maria db", '[{"LOWER": "maria"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "IBM Informix": [
        ("informix", '[{"LOWER": "informix"}]'),
    ],
    "SAP HANA": [
        ("sap hana", '[{"LOWER": "sap"}, {"LOWER": "hana"}]'),
    ],
    "Apache Derby": [
        ("apache derby", '[{"LOWER": "apache"}, {"LOWER": "derby"}]'),
    ],
    "Firebird": [
        ("firebird", '[{"LOWER": "firebird"}]'),
    ],
    "Apache Cassandra": [
        ("cassandra", '[{"LOWER": "cassandra"}]'),
    ],
    "CockroachDB": [
        ("cockroachdb", '[{"LOWER": "cockroachdb"}]'),
        ("cockroach db", '[{"LOWER": "cockroach"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "Microsoft Access": [
        ("microsoft access", '[{"LOWER": "microsoft"}, {"LOWER": "access"}]'),
        ("Access", '[{"IS_TITLE": true, "LOWER": "access"}]'),
    ],
    "Vertica": [
        ("vertica", '[{"LOWER": "vertica"}]'),
    ],
    "Amazon Aurora": [
        ("amazon aurora", '[{"LOWER": "amazon"}, {"LOWER": "aurora"}]'),
    ],
    "Apache CouchDB": [
        ("couchdb", '[{"LOWER": "couchdb"}]'),
        ("couch db", '[{"LOWER": "couch"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "Apache HBase": [
        ("hbase", '[{"LOWER": "hbase"}]'),
    ],
    "Couchbase": [
        ("couchbase", '[{"LOWER": "couchbase"}]'),
    ],
    "ArangoDB": [
        ("arangodb", '[{"LOWER": "arangodb"}]'),
        ("arango db", '[{"LOWER": "arango"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "Aerospike": [
        ("aerospike", '[{"LOWER": "aerospike"}]'),
    ],
    "Riak": [
        ("riak", '[{"LOWER": "riak"}]'),
    ],
    "MarkLogic": [
        ("marklogic", '[{"LOWER": "marklogic"}]'),
    ],
    "Extensible Markup Language (XML)": [
        ("xml", '[{"LOWER": "xml"}]'),
    ],
    "Google Cloud Datastore": [
        ("google cloud datastore", '[{"LOWER": "google"}, {"LOWER": "cloud"}, {"LOWER": "datastore"}]'),
    ],
    "FaunaDB": [
        ("faunadb", '[{"LOWER": "faunadb"}]'),
        ("fauna db", '[{"LOWER": "fauna"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "Apache Ignite": [
        ("ignite", '[{"LOWER": "ignite"}]'),
    ],
    "GridGain": [
        ("gridgain", '[{"LOWER": "gridgain"}]'),
    ],
    "VoltDB": [
        ("voltdb", '[{"LOWER": "voltdb"}]'),
        ("volt db", '[{"LOWER": "volt"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "MemSQL": [
        ("memsql", '[{"LOWER": "memsql"}]'),
    ],
    "Android Studio": [
        ("android studio", '[{"LOWER": "android"}, {"LOWER": "studio"}]'),
        ("android sdk", '[{"LOWER": "android"}, {"LOWER": "sdk"}]'),
    ],
    "Ansible": [
        ("ansible", '[{"LOWER": "ansible"}]'),
    ],
    "Ant": [
        ("ant", '[{"LOWER": "ant"}]'),
    ],
    "Apache Kafka": [
        ("kafka", '[{"LOWER": "kafka"}]'),
    ],
    "Rational ClearCase": [
        ("clearcase", '[{"LOWER": "clearcase"}]'),
        ("clear case", '[{"LOWER": "clear"}, {"LOWER": "case"}]'),
    ],
    "Confluence": [
        ("confluence", '[{"LOWER": "confluence"}]'),
    ],
    "Crystal Reports": [
        ("crystal reports", '[{"LOWER": "crystal"}, {"LOWER": "reports"}]'),
    ],
    "Customer Relationship Management (CRM)": [
        ("customer relationship management", '[{"LOWER": "customer"}, {"LOWER": "relationship"}, {"LOWER": "management"}]'),
        ("crm", '[{"LOWER": "crm"}]'),
    ],
    "Docker": [
        ("docker", '[{"LOWER": "docker"}]'),
    ],
    "E-commerce": [
        ("ecommerce", '[{"LOWER": "ecommerce"}]'),
        ("e-commerce", '[{"LOWER": "e"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "commerce"}]'),
    ],
    "Eclipse IDE": [
        ("eclipse", '[{"LOWER": "eclipse"}]'),
    ],
    "Enterprise Resource Planning (ERP)": [
        ("enterprise resource planning", '[{"LOWER": "enterprise"}, {"LOWER": "resource"}, {"LOWER": "planning"}]'),
        ("erp", '[{"LOWER": "erp"}]'),
    ],
    "Firmware": [
        ("firmware", '[{"LOWER": "firmware"}]'),
    ],
    "Git Version Control": [
        ("git", '[{"LOWER": "git"}]'),
    ],
    "Hadoop": [
        ("hadoop", '[{"LOWER": "hadoop"}]'),
    ],
    "Internet Information Services (IIS)": [
        ("internet information services", '[{"LOWER": "internet"}, {"LOWER": "information"}, {"LOWER": "services"}]'),
        ("iis", '[{"LOWER": "iis"}]'),
    ],
    "IntelliJ IDEA": [
        ("intellij", '[{"LOWER": "intellij"}]'),
    ],
    "iPhone OS (iOS)": [
        ("ios", '[{"LOWER": "ios"}]'),
        ("iphone os", '[{"LOWER": "iphone"}, {"LOWER": "os"}]'),
    ],
    "JBoss": [ 
        ("jboss", '[{"LOWER": "jboss"}]'),
    ],
    "Jenkins": [ 
        ("jenkins", '[{"LOWER": "jenkins"}]'),
    ],
    "JIRA": [
        ("jira", '[{"LOWER": "jira"}]'),
    ],
    "Kubernetes": [
        ("kubernetes", '[{"LOWER": "kubernetes"}]'),
    ],
    "Linux": [
        ("linux", '[{"LOWER": "linux"}]'),
        ("ubuntu", '[{"LOWER": "ubuntu"}]'),
        ("red hat", '[{"LOWER": "red"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "hat"}]'),
        ("redhat", '[{"LOWER": "redhat"}]'),
        ("centos", '[{"LOWER": "centos"}]'),
        ("debian", '[{"LOWER": "debian"}]'),
    ],
    "Maven": [
        ("maven", '[{"LOWER": "maven"}, {"LOWER": "mvn"}]'),
    ],
    "Microsoft Azure": [
        ("azure", '[{"LOWER": "azure"}]'),
    ],
    "Microsoft Excel": [
        ("excel", '[{"LOWER": "excel"}]'),
    ],
    "Microsoft Office": [
        ("microsoft office", '[{"LOWER": {"IN": ["microsoft", "ms"]} }, {"LOWER": "office"}]'),
        ("msoffice", '[{"LOWER": "msoffice"}]'),
    ],
    "Microsoft PowerPoint": [
        ("powerpoint", '[{"LOWER": "powerpoint"}]'),
        ("power point", '[{"LOWER": "power"}, {"LOWER": "point"}]'),
    ],
    "Microsoft Word": [
        ("microsoft word", '[{"LOWER": "microsoft"}, {"LOWER": "word"}]'),
    ],
    "Microsoft Project": [
        ("ms project", '[{"LOWER": {"IN": ["microsoft", "ms"]} }, {"LOWER": "project"}]'),
        ("msproject", '[{"LOWER": "msproject"}]'),
    ],
    "Perforce": [
        ("perforce", '[{"LOWER": "perforce"}]'),
    ],
    "Salesforce": [
        ("salesforce", '[{"LOWER": "salesforce"}]'),
        ("salesforce.com", '[{"LOWER": "salesforce.com"}]'),
        ("sales force", '[{"LOWER": "sales"}, {"LOWER": "force"}]'),
    ],
    "Microsoft SharePoint": [
        ("sharepoint", '[{"LOWER": "sharepoint"}]'),
        ("share point", '[{"LOWER": "share"}, {"LOWER": "point"}]'),
    ],
    "Solaris": [
        ("solaris", '[{"LOWER": "solaris"}]'),
    ],
    "Solidworks": [
        ("solidworks", '[{"LOWER": "solidworks"}]'),
    ],
    "Tableau": [
        ("tableau", '[{"LOWER": "tableau"}]'),
    ],
    "Team Foundation Server (TFS)": [
        ("team foundation server", '[{"LOWER": "team"}, {"LOWER": "foundation"}, {"LOWER": "server"}]'),
        ("tfs", '[{"LOWER": "tfs"}]'),
    ],
    "Terraform": [
        ("terraform", '[{"LOWER": "terraform"}]'),
    ],
    "Apache Tomcat": [
        ("tomcat", '[{"LOWER": "tomcat"}]'),
    ],
    "Tortoise SVN": [
        ("tortoise", '[{"LOWER": "tortoise"}]'),
    ],
    "Unix": [
        ("unix", '[{"LOWER": "unix"}]'),
    ],
    "Microsoft Visio": [
        ("visio", '[{"LOWER": "visio"}]'),
        ("msvisio", '[{"LOWER": "msvisio"}]'),
    ],
    "Microsoft Visual Studio": [
        ("visual studio", '[{"LOWER": "visual"}, {"LOWER": "studio"}]'),
    ],
    "VMware": [
        ("vmware", '[{"LOWER": "vmware"}]'),
    ],
    "WebLogic": [ 
        ("weblogic", '[{"LOWER": "weblogic"}]'),
    ],
    "Microsoft Windows": [
        ("microsoft windows", '[{"LOWER": {"IN": ["microsoft", "ms"]} }, {"LOWER": "windows"}]'),
        ("windows 7", '[{"LOWER": "windows"}, {"LIKE_NUM": true}]'),
    ],
    "Microsoft Windows Server": [
        ("windows server", '[{"LOWER": "windows"}, {"LOWER": "server"}]'),
    ],
    "Xcode": [
        ("xcode", '[{"LOWER": "xcode"}]'),
        ("x code", '[{"LOWER": "x"}, {"LOWER": "code"}]'),
    ],
    "VSCode": [
        ("vscode", '[{"LOWER": "vscode"}]'),
        ("vs code", '[{"LOWER": "vs"}, {"LOWER": "code"}]'),
    ],
    "Agile Methodologies": [
        ("agile", '[{"LOWER": "agile"}]'),
    ],
    "Algorithms Programming": [
        ("algorithm", '[{"LOWER": "algorithm"}]'),
        ("algorithms", '[{"LOWER": "algorithms"}]'),
    ],
    "Customer Service": [
        ("customer service", '[{"LOWER": "customer"}, {"LOWER": "service"}]'),
    ],
    "Strategic Partnerships": [
        ("strategic partnerships", '[{"LOWER": "strategic"}, {"LOWER": "partnerships"}]'),
        ("strategic partnership", '[{"LOWER": "strategic"}, {"LOWER": "partnership"}]'),
    ],
    "Amazon Web Services (AWS)": [
        ("aws", '[{"LOWER": "aws"}]'),
        ("amazon web services", '[{"LOWER": "amazon"}, {"LOWER": "web"}, {"LOWER": "services"}]'),
    ],
     "Android Development": [
        ("android development", '[{"LOWER": "android"}, {"LOWER": "development"}]'),
    ],
    "API Development": [
        ("api development", '[{"LOWER": "api"}, {"LOWER": "development"}]'),
    ],
     "Software Development": [
        ("application development", '[{"LOWER": {"IN": ["application", "software", "product"]} }, {"LOWER": "development"}]'),
    ],
    "Software Architecture": [
        ("software architecture", '[{"LOWER": {"IN": ["application", "software", "system", "solution"]} }, {"LOWER": "architecture"}]'),
        ("architectural design", '[{"LOWER": {"IN": ["architectural", "architecture"]} }, {"LOWER": "design"}]'),
    ],
    "Artificial Intelligence (AI)": [
        ("ai", '[{"LOWER": "ai"}]'),
        ("artificial intelligence", '[{"LOWER": "artificial"}, {"LOWER": "intelligence"}]'),
    ],
    "Critical Thinking": [
        ("critical thinking", '[{"LOWER": "critical"}, {"LOWER": "thinking"}]'),
    ],
    "BackEnd Development": [ 
        ("backend", '[{"LOWER": "backend"}]'),
        ("back-end", '[{"LOWER": "back"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "end"}]'),
    ],
    "Big Data": [
        ("bigdata", '[{"LOWER": "bigdata"}]'),
        ("big data", '[{"LOWER": "big"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "data"}]'),
    ],
    "Business Analysis": [
        ("business analysis", '[{"LOWER": "business"}, {"LOWER": "analysis"}]'),
    ],
    "Business Intelligence (BI)": [
        ("business intelligence", '[{"LOWER": "business"}, {"LOWER": "intelligence"}]'),
        ("bi", '[{"LOWER": "bi"}]'),
    ],
    "Cloud Computing": [
        ("cloud computing", '[{"LOWER": "cloud"}, {"LOWER": "computing"}]'),
    ],
    "Continuous Integration and Continuous Delivery (CI/CD)": [
        ("continuous integration", '[{"LOWER": "continuous"}, {"LOWER": "integration"}]'),
        ("continuous delivery", '[{"LOWER": "continuous"}, {"LOWER": "delivery"}]'),
        ("ci/cd", '[{"LOWER": "ci"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "cd"}]'),
    ],
    "Data Mining": [
        ("data mining", '[{"LOWER": "data"}, {"LOWER": "mining"}]'),
    ],
     "Data Modeling": [
        ("data modeling", '[{"LOWER": "data"}, {"LOWER": "modeling"}]'),
    ],
    "Data Science": [
        ("data science", '[{"LOWER": "data"}, {"LOWER": "science"}]'),
    ],
    "Data Structures": [
        ("data structures", '[{"LOWER": "data"}, {"LOWER": {"IN": ["structures", "structure"]}}]'),
    ],
    "Data Visualization": [
        ("data visualization", '[{"LOWER": "data"}, {"LOWER": "visualization"}]'),
    ],
    "Database Administration": [
        ("database administration", '[{"LOWER": "database"}, {"LOWER": "administration"}]'),
    ],
    "Database Design": [
        ("database design", '[{"LOWER": "database"}, {"LOWER": "design"}]'),
    ],
    "Database Modeling": [
        ("database modeling", '[{"LOWER": "database"}, {"LOWER": "modeling"}]'),
    ],
    "Debugging": [
        ("debugging", '[{"LOWER": "debugging"}]'),
    ],
    "Deep Learning": [
        ("deep learning", '[{"LOWER": "deep"}, {"LOWER": "learning"}]'),
    ],
    "Design Patterns": [
        ("design patterns", '[{"LOWER": "design"}, {"LOWER": {"IN": ["patterns", "pattern"]} }]'),
    ],
    "DevOps": [
        ("devops", '[{"LOWER": "devops"}]'),
    ],
    "Disaster Recovery": [
        ("disaster recovery", '[{"LOWER": "disaster"}, {"LOWER": "recovery"}]'),
    ],
    "Distributed Systems": [
        ("distributed systems", '[{"LOWER": "distributed"}, {"LOWER": {"IN": ["system", "systems"]} }]'),
    ],
    "Engineering/Development Management": [
        ("engineering management", '[{"LOWER": {"IN": ["engineering", "development"]} }, {"LOWER": "management"}]'),
    ],
    "Enterprise Architecture": [
        ("enterprise architecture", '[{"LOWER": "enterprise"}, {"LOWER": "architecture"}]'),
    ],
    "Extract Transform Load (ETL)": [
        ("etl", '[{"LOWER": "etl"}]'),
    ],
    "FrontEnd Development": [
        ("frontend", '[{"LOWER": "frontend"}]'),
        ("front-end", '[{"LOWER": "front"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "end"}]'),
    ],
     "FullStack Development": [
        ("fullstack", '[{"LOWER": "fullstack"}]'),
        ("full-stack", '[{"LOWER": "full"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "stack"}]'),
    ],
    "Game Design": [
        ("game design", '[{"LOWER": "game"}, {"LOWER": "design"}]'),
    ],
    "Game Development": [
        ("game development", '[{"LOWER": "game"}, {"LOWER": "development"}]'),
    ],
    "Google Cloud Platform (GCP)": [
        ("google cloud", '[{"LOWER": "google"}, {"LOWER": "cloud"}]'),
        ("gcp", '[{"LOWER": "gcp"}]'),
    ],
    "Information Security": [
        ("information security", '[{"LOWER": "information"}, {"LOWER": "security"}]'),
    ],
    "iOS Development": [
        ("ios development", '[{"LOWER": "ios"}, {"LOWER": "development"}]'),
    ],
    "IT Management": [
        ("it management", '[{"LOWER": "it"}, {"LOWER": "management"}]'),
        ("it service management", '[{"LOWER": "it"}, {"LOWER": "service"}, {"LOWER": "management"}]'),
        ("information technology management", '[{"LOWER": "information"}, {"LOWER": "technology"}, {"LOWER": "management"}]'),
    ],
     "Information Technology Infrastructure Library (ITIL)": [
        ("information technology infrastructure library", '[{"LOWER": "information"}, {"LOWER": "technology"}, {"LOWER": "infrastructure"}, {"LOWER": "library"}]'),
        ("itil", '[{"LOWER": "itil"}]'),
    ],
    "Machine Learning": [
        ("machine learning", '[{"LOWER": "machine"}, {"LOWER": "learning"}]'),
    ],
    "Microservices": [
        ("microservices", '[{"LOWER": {"IN": ["microservices", "microservice"]} }]'),
    ],
       "Mobile Development": [
        ("mobile application development", '[{"LOWER": "mobile"}, {"LOWER": {"IN": ["application", "applications"]}, "OP": "?"}, {"LOWER": "development"}]'),
    ],
    "Multithreading": [
        ("multithreading", '[{"LOWER": "multithreading"}]'),
        ("multi-threading", '[{"LOWER": "multi"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "threading"}]'),
    ],
     "Network Administration": [
        ("networking administration", '[{"LOWER": "networking"}, {"LOWER": "administration"}]'),
    ],
    "NoSQL Databases": [
        ("nosql", '[{"LOWER": "nosql"}]'),
    ],
    "Object-Oriented Programming (OOP)": [
        ("object-oriented", '[{"LOWER": "object"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "oriented"}]'),
        ("oop", '[{"LOWER": "oop"}]'),
    ],
    "Project Management Professional (PMP)": [
        ("project management professional", '[{"LOWER": "project"}, {"LOWER": "management"}, {"LOWER": "professional"}]'),
        ("pmp", '[{"LOWER": "pmp"}]'),
    ],
    "MacOS": [
        ("macos", '[{"LOWER": "macos"}]'),
        ("mac os:", '[{"LOWER": "mac"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "os"}]'),
        ("os x", '[{"LOWER": "os"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "x"}]'),
    ],
    "Product Management": [
        ("product management", '[{"LOWER": {"IN": ["product", "program"]} }, {"LOWER": "management"}]'),
    ],
    "Project Management": [
        ("project management", '[{"LOWER": "project"}, {"LOWER": "management"}]'),
    ],
    "Project Planning": [
        ("project planning", '[{"LOWER": "project"}, {"LOWER": "planning"}]'),
    ],
    "Relational Databases": [
        ("relational databases", '[{"LOWER": "relational"}, {"LOWER": "databases"}]'),
    ],
    "REST API WebServices": [
        ("restful", '[{"LOWER": {"IN": ["restful", "rest"]} }]'),
        ("representational state transfer", '[{"LOWER": "representational"}, {"LOWER": "state"}, {"LOWER": "transfer"}]'),
    ],
    "Requirements Analysis": [
        ("requirements analysis", '[{"LOWER": {"IN": ["requirements", "requirement"]} }, {"LOWER": "analysis"}]'),
        ("business requirements", '[{"LOWER": "business"}, {"LOWER": {"IN": ["requirements", "requirement"]} }]'),
    ],
     "Requirements Gathering": [
        ("requirements gathering", '[{"LOWER": {"IN": ["requirements", "requirement"]} }, {"LOWER": "gathering"}]'),
    ],
    "Robotics": [
        ("robotics", '[{"LOWER": {"IN": ["robotics", "robotic"]} }]'),
    ],
    "Software as a Service (SASS)": [
        ("sofware as a service", '[{"LOWER": "sofware"}, {"LOWER": "as"}, {"LOWER": "a"}, {"LOWER": "service"}]'),
        ("sass", '[{"LOWER": "sass"}]'),
    ],
    "Scalability": [
        ("scalability", '[{"LOWER": "scalability"}]'),
    ],
    "Scrum": [
        ("scrum", '[{"LOWER": "scrum"}]'),
    ],
    "Software Development Lifecycle (SDLC)": [
        ("software development lifecycle", '[{"LOWER": {"IN": ["sofware", "application"]} }, {"LOWER": "development", "OP": "?"}, {"LOWER": {"IN": ["lifecycle", "life"]} }, {"LOWER": "cycle", "OP": "?"}]'),
        ("sdlc", '[{"LOWER": "sdlc"}]'),
        ("alm", '[{"LOWER": "alm"}]'),
    ],
    "Search Engine Optimization (SEO)": [
        ("search engine optimization", '[{"LOWER": "search"}, {"LOWER": "engine"}, {"LOWER": "optimization"}]'),
        ("seo", '[{"LOWER": "seo"}]'),
    ],
    "Service Oriented Architecture (SOA)": [
        ("service oriented architecture", '[{"LOWER": "service"}, {"LOWER": "oriented"}, {"LOWER": "architecture"}]'),
        ("soa", '[{"LOWER": "soa"}]'),
    ],
    "Simple Object Access Protocol (SOAP)": [
        ("soap", '[{"LOWER": "soap"}]'),
    ],
    "Software Design": [
        ("software design", '[{"LOWER": "software"}, {"LOWER": "design"}]'),
    ],
    "Application Security": [
        ("application security", '[{"LOWER": "application"}, {"LOWER": {"IN": ["security", "vulnerabilities", "vulnerability"]} }]'),
    ],
     "Software Documentation": [
        ("software documentation", '[{"LOWER": {"IN": ["software", "technical"]} }, {"LOWER": "documentation"}]'),
    ],
     "Software Engineering": [
        ("software engineering", '[{"LOWER": {"IN": ["software", "system", "systems"]} }, {"LOWER": "engineering"}]'),
    ],
    "Software Project Management": [
        ("software project management", '[{"LOWER": "software"}, {"LOWER": "project"}, {"LOWER": "management"}]'),
    ],
    "Software Quality Assurance": [
        ("software quality assurance", '[{"LOWER": "software"}, {"LOWER": "quality"}, {"LOWER": "assurance"}]'),
    ],
    "Software Testing": [
        ("software testing", '[{"LOWER": {"IN": ["software", "regression", "blackbox", "functional", "unit", "manual", "api"]} }, {"LOWER": {"IN": ["testing", "test", "tests"]} }]'),
        ("test cases", '[{"LOWER": {"IN": ["testing", "test", "tests"]} }, {"LOWER": {"IN": ["cases", "automation", "planning"]} }]'),
        ("user acceptance testing", '[{"LOWER": "user"}, {"LOWER": "acceptance"}, {"LOWER": {"IN": ["testing", "test", "tests"]} }]'),
        ("black box testing", '[{"LOWER": "black"}, {"LOWER": "box"}, {"LOWER": {"IN": ["testing", "test", "tests"]} }]'),

    ],
    "Team Management": [
        ("team management", '[{"LOWER": "team"}, {"LOWER": "management"}]'),
    ],
    "Technical Leadership": [
        ("technical leadership", '[{"LOWER": "technical"}, {"LOWER": "leadership"}]'),
    ],
    "Technical Support": [
        ("technical support", '[{"LOWER": "technical"}, {"LOWER": "support"}]'),
    ],
    "Technical Writing": [
        ("technical writing", '[{"LOWER": "technical"}, {"LOWER": "writing"}]'),
    ],
     "Web Development": [
        ("web application development", '[{"LOWER": "web"}, {"LOWER": "application", "OP": "?"}, {"LOWER": {"IN": ["development", "design"]} }]'),
    ],
    "Web Services": [
        ("web services", '[{"LOWER": "web"}, {"LOWER": "services"}]'),
    ],
    "User Experience (UI) and User Interface (UX) Design": [
        ("user experience", '[{"LOWER": "user"}, {"LOWER": {"IN": ["experience", "interface"]} }]'),
        ("ux design", '[{"LOWER": {"IN": ["ux", "ui"]} }, {"LOWER": "design"}]'),
        ("ui/ux", '[{"LOWER": {"IN": ["ux", "ui"]} }, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": {"IN": ["ux", "ui"]} }]'),
    ],
     "Unified Modeling Language (UML)": [
        ("unified modeling language", '[{"LOWER": "unified"}, {"LOWER": "modeling"}, {"LOWER": "language"}]'),
        ("uml", '[{"LOWER": "uml"}]'),
    ],
    "eXtensible Stylesheet Language for Transformation (XSLT)": [
        ("xslt", '[{"LOWER": "xslt"}]'),
    ],
    "Lamport TeX (LaTeX)": [
        ("latex", '[{"LOWER": "latex"}]'),
    ],
    "Automation": [
        ("automation", '[{"LOWER": "automation"}]'),
    ],
    "Computer Hardware": [
        ("hardware", '[{"LOWER": "hardware"}]'),
    ],
    "Cyber Security": [
        ("cyber security", '[{"LOWER": "cyber"}, {"LOWER": "security"}]'),
        ("cybersecurity", '[{"LOWER": "cybersecurity"}]'),
    ],
    "Data Analysis": [
        ("data analysis", '[{"LOWER": "data"}, {"LOWER": "analysis"}]'),
    ],
    "Entrepreneurship": [
        ("entrepreneurship", '[{"LOWER": "entrepreneurship"}]'),
    ],
    "Google Analytics": [
        ("google analytics", '[{"LOWER": "google"}, {"LOWER": "analytics"}]'), 
    ],
    "Graphic Design": [
        ("graphic design", '[{"LOWER": "graphic"}, {"LOWER": "design"}]'),
    ],
    "Leadership": [
        ("leadership", '[{"LOWER": "leadership"}]'),
    ],
    "Mentoring and Training": [
        ("mentoring", '[{"LOWER": "mentoring"}]'),
        ("teaching", '[{"LOWER": "teaching"}]'),
        ("coaching", '[{"LOWER": "coaching"}]'),
        ("training", '[{"LOWER": "training"}]'),
    ],
    "Problem Solving": [
        ("problem solving", '[{"LOWER": "problem"}, {"LOWER": "solving"}]'),
    ],
    "Process Improvement": [
        ("process improvement", '[{"LOWER": "process"}, {"LOWER": "improvement"}]'),
    ],
    "Public Speaking": [
        ("public speaking", '[{"LOWER": "public"}, {"LOWER": "speaking"}]'),
    ],
    "Quality Assurance": [
        ("quality assurance", '[{"LOWER": "quality"}, {"LOWER": "assurance"}]'),
    ],
    "Research": [
        ("research", '[{"LOWER": "research"}]'),
    ],
    "Statistics": [
        ("statistics", '[{"LOWER": "statistics"}]'),
    ],
    "System Administration": [
        ("system administration", '[{"LOWER": {"IN": ["system", "systems"]} }, {"LOWER": "administration"}]'),
    ],
    "Systems Analysis": [
        ("systems analysis", '[{"LOWER": {"IN": ["system", "systems"]} }, {"LOWER": "analysis"}]'),
        ("analysis services", '[{"LOWER": "analysis"}, {"LOWER": "services"}]'),
    ],    
    "Team Building": [
        ("team building", '[{"LOWER": "team"}, {"LOWER": "building"}]'),
    ],
    "Team Player": [
        ("teamwork", '[{"LOWER": {"IN": ["teamwork", "teamplayer", "collaborative"]} }]'),
        ("team work", '[{"LOWER": "team"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": {"IN": ["work", "player"]} }]'),
    ],
    "Telecommunications": [
        ("telecommunications", '[{"LOWER": {"IN": ["telecommunication", "telecommunications"]} }]'),
    ],
    "Time Management": [
        ("time management", '[{"LOWER": "time"}, {"LOWER": "management"}]'),
    ],
    ".NET Framework": [
        ("dotnet framework", '[{"LOWER": {"IN": ["dotnet", ".net", "net"]} }, {"LOWER": "framework"}]'),
        ("dot net framework", '[{"LOWER": "dot"}, {"LOWER": "net"}, {"LOWER": "framework"}]'),
    ],
    "JavaScript Object Notation (JSON)": [
        ("javaScript object notation", '[{"LOWER": "javaScript"}, {"LOWER": "object"}, {"LOWER": "notation"}]'),
        ("json", '[{"LOWER": "json"}]'),
    ],
    "Troubleshooting": [
        ("troubleshooting", '[{"LOWER": "troubleshooting"}]'),
    ],
    "Strategic Planning":[
        ("strategic planning", '[{"LOWER": "strategic"}, {"LOWER": "planning"}]'),
    ],
    "Enterprise Software":[
        ("enterprise software", '[{"LOWER": "enterprise"}, {"LOWER": "software"}]'),
    ],
    "Communication":[
        ("communication", '[{"LOWER": "communication"}]'),
    ],
    "Apache Subversion (SVN)":[
        ("apache subversion", '[{"LOWER": "apache"}, {"LOWER": "subversion"}]'),
        ("svn", '[{"LOWER": "svn"}]'),
    ],
    "GitHub":[
        ("github", '[{"LOWER": "github"}]'),
    ],
    "GitLab":[
        ("gitlab", '[{"LOWER": "gitlab"}]'),
    ],
    "Embedded Systems":[
        ("embedded systems", '[{"LOWER": "embedded"}, {"LOWER": {"IN": ["systems", "system", "software"]} }]'),
    ],
    "Application Programming Interfaces (API)":[
        ("application programming interfaces", '[{"LOWER": "application"}, {"LOWER": "programming"}, {"LOWER": "interfaces"}]'),
        ("api", '[{"LOWER": "api"}]'),
    ],
    "Recruiting":[
        ("recruiting", '[{"LOWER": "recruiting"}]'),
    ],
    "Shell Scripting":[
        ("shell scripting", '[{"LOWER": "shell"}, {"LOWER": {"IN": ["scripting", "script"]} }]'),
    ],
    "Cross-functional Team Leadership":[
        ("cross functional team leadership", '[{"LOWER": "cross"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "functional"}, {"LOWER": "team"}, {"LOWER": "leadership"}]'),
    ],
    "Business Development":[
        ("business development", '[{"LOWER": "business"}, {"LOWER": "development"}]'),
    ],
    "Computer Science Fundamentals":[
        ("computer science", '[{"LOWER": "computer"}, {"LOWER": "science"}]'),
    ],
    "Test Driven Development (TDD)":[
        ("test driven development", '[{"LOWER": "test"}, {"LOWER": "driven"}, {"LOWER": "development"}]'),
        ("tdd", '[{"LOWER": "tdd"}]'),
    ],
     "Marketing":[
        ("marketing", '[{"LOWER": "marketing"}]'),
    ],
    "Data Warehousing":[
        ("data warehousing", '[{"LOWER": "data"}, {"LOWER": "warehousing"}]'),
    ],
    "Vendor Management":[
        ("vendor management", '[{"LOWER": "vendor"}, {"LOWER": "management"}]'),
    ],
    "Consulting":[
        ("consulting", '[{"LOWER": "consulting"}]'),
    ],
    "Business Strategy":[
        ("business strategy", '[{"LOWER": "business"}, {"LOWER": "strategy"}]'),
    ],
    "Microsoft Active Directory":[
        ("active directory", '[{"LOWER": "active"}, {"LOWER": "directory"}]'),
    ],
    "Transmission Control Protocol/Internet Protocol (TCP/IP)": [
        ("transmission control protocol", '[{"LOWER": "transmission"}, {"LOWER": "control"}, {"LOWER": "protocol"}]'),
        ("internet protocol", '[{"LOWER": "internet"}, {"LOWER": "protocol"}]'),
        ("tcp/ip", '[{"LOWER": "tcp"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "ip"}]'),
    ],
    "Startup Environment":[
        ("startup", '[{"LOWER": "startup"}]'),
        ("startups", '[{"LOWER": "startups"}]'),
        ("start-ups", '[{"LOWER": "start"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "ups"}]'),
        ("start-up", '[{"LOWER": "start"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "up"}]'),
    ],
    "Analytical Skills":[
        ("analytical skills", '[{"LOWER": "analytical"}, {"LOWER": {"IN": ["skills", "skill"]} }]'),
    ],
    "Information Technology Strategy":[
        ("information technology strategy", '[{"LOWER": "information"}, {"LOWER": "technology"}, {"LOWER": "strategy"}]'),
        ("it strategy", '[{"LOWER": "it"}, {"LOWER": "strategy"}]'),
    ],
    "Change Management":[
        ("change management", '[{"LOWER": "change"}, {"LOWER": "management"}]'),
    ],
    "Virtualization":[
        ("virtualization", '[{"LOWER": "virtualization"}]'),
    ],
    "Account Management":[
        ("account management", '[{"LOWER": "account"}, {"LOWER": "management"}]'),
    ],
    "AutoCAD":[
        ("autocad", '[{"LOWER": "autocad"}]'),
    ],
    "English":[
        ("english", '[{"LOWER": "english"}]'),
    ],
    "Network Security": [
        ("network security", '[{"LOWER": "network"}, {"LOWER": "security"}]'),
    ],
    "Marketing Strategy": [
        ("marketing strategy", '[{"LOWER": "marketing"}, {"LOWER": "strategy"}]'),
    ],
    "Manufacturing Processes": [
        ("manufacturing", '[{"LOWER": "manufacturing"}]'),
    ],
    "Adobe Photoshop": [
        ("photoshop", '[{"LOWER": "photoshop"}]'),
    ],
    "Operations Management": [
        ("operations management", '[{"LOWER": "operations"}, {"LOWER": "management"}]'),
    ],
    ".NET Core": [
        ("dotnet core", '[{"LOWER": "dotnet"}, {"LOWER": "core"}]'),
        (".net core", '[{"LOWER": ".net"}, {"LOWER": "core"}]'),
        ("dot net core", '[{"LOWER": "dot"}, {"LOWER": "net"}, {"LOWER": "core"}]'),
    ],
    "Sales Management": [
        ("sales management", '[{"LOWER": "sales"}, {"LOWER": "management"}]'),
    ],
    "Data Center Operations": [
        ("data center", '[{"LOWER": "data"}, {"LOWER": "center"}]'),
    ],
    "Event Planning": [
        ("event planning", '[{"LOWER": "event"}, {"LOWER": "planning"}]'),
    ],
    "Social Media Marketing": [
        ("social media marketing", '[{"LOWER": "social"}, {"LOWER": "media"}, {"LOWER": "marketing"}]'),
    ],
    "Adobe Creative Suite": [
        ("adobe creative suite", '[{"LOWER": "adobe"}, {"LOWER": "creative"}, {"LOWER": "suite"}]'),
    ],
    "Data Analytics": [
        ("data analytics", '[{"LOWER": "data"}, {"LOWER": "analytics"}]'),
    ],
    "Risk Management": [
        ("risk management", '[{"LOWER": "risk"}, {"LOWER": "management"}]'),
    ],
    "Simulations": [
        ("simulations", '[{"LOWER": "simulations"}]'),
    ],
    "Contract Negotiation": [
        ("contract negotiation", '[{"LOWER": "contract"}, {"LOWER": "negotiation"}]'),
    ],
    "Device Drivers Engineering": [
        ("device drivers", '[{"LOWER": "device"}, {"LOWER": {"IN": ["drivers", "driver"]} }]'),
    ],
    "Computer Vision": [
        ("computer vision", '[{"LOWER": "computer"}, {"LOWER": "vision"}]'),
    ],
    "Amazon Elastic Compute Cloud (Amazon EC2)": [
        ("amazon ec2", '[{"LOWER": "ec2"}]'),
        ("elastic compute cloud", '[{"LOWER": "elastic"}, {"LOWER": "compute"}, {"LOWER": "cloud"}]'),
    ],
    "AWS Lambda": [
        ("aws lambda", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "lambda"}]'),
    ],
    "AWS Batch": [
        ("aws batch", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "batch"}]'),
    ],
    "Amazon Lightsail": [
        ("amazon lightsail", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "lightsail"}]'),
    ],
    "AWS Elastic Beanstalk": [
        ("aws elastic beanstalk", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "elastic"}, {"LOWER": "beanstalk"}]'),
    ],
    "AWS Fargate": [
        ("aws fargate", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "fargate"}]'),
    ],
    "AWS Outposts": [
        ("aws outposts", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "outposts"}]'),
    ],
    "AWS Serverless Application Repository": [
        ("aws serverless application repository", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "serverless"}, {"LOWER": "application"}, {"LOWER": "repository"}]'),
    ],
    "AWS Snow Family": [
        ("aws snow", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "snow"}]'),
    ],
    "Amazon Simple Storage Service (Amazon S3)": [
        ("amazon s3", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "s3"}]'),
        ("simple storage service", '[{"LOWER": "simple"}, {"LOWER": "storage"}, {"LOWER": "service"}]'),
    ],
    "Amazon Elastic Block Store (Amazon EBS)": [
        ("amazon ebs", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "ebs"}]'),
        ("elastic block store", '[{"LOWER": "elastic"}, {"LOWER": "block"}, {"LOWER": "store"}]'),
    ],
    "Amazon Elastic File System (Amazon EFS)": [
        ("amazon efs", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "efs"}]'),
        ("elastic file system", '[{"LOWER": "elastic"}, {"LOWER": "file"}, {"LOWER": "system"}]'),
    ],
    "Amazon File Systems (Amazon FSx)": [
        ("amazon fsx", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "fsx"}]'),
        ("amazon file systems", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "file"}, {"LOWER": "systems"}]'),
    ],
    "Amazon S3 Glacier": [
        ("amazon glacier", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "glacier"}]'),
        ("s3 glacier", '[{"LOWER": "s3"}, {"LOWER": "glacier"}]'),
    ],
    "AWS Storage Gateway": [
        ("aws storage gateway", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "storage"}, {"LOWER": "gateway"}]'),
    ],
    "AWS Backup": [
        ("aws backup", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "backup"}]'),
    ],
    "Amazon Relational Database Service (Amazon RDS)": [
        ("amazon rds", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "rds"}]'),
        ("relational database service", '[{"LOWER": "relational"}, {"LOWER": "database"}, {"LOWER": "service"}]'),
    ],
    "Amazon DynamoDB": [
        ("dynamodb", '[{"LOWER": "dynamodb"}]'),
        ("dynamo db", '[{"LOWER": "dynamo"}, {"LOWER": {"IN": ["db", "database"]} }]'),
    ],
    "Amazon ElastiCache": [
        ("elasticache", '[{"LOWER": "elasticache"}]'),
    ],
    "Amazon Neptune": [
        ("amazon neptune", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "neptune"}]'),
    ],
    "Amazon Redshift": [
        ("redshift", '[{"LOWER": "redshift"}]'),
    ],
    "AWS Database Migration Service (Amazon DMS)": [
        ("database migration service", '[{"LOWER": "database"}, {"LOWER": "migration"}, {"LOWER": "service"}]'),
        ("aws dms", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "dms"}]'),
    ],
    "AWS DocumentDB": [
        ("documentdb", '[{"LOWER": "documentdb"}]'),
        ("document db", '[{"LOWER": "document"}, {"LOWER": "db"}]'),
    ],
    "AWS Timestream": [
        ("amazon timestream", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "timestream"}]'),
    ],
    "Amazon Virtual Private Cloud (Amazon VPC)": [
        ("amazon vpc", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "vpc"}]'),
        ("virtual private cloud", '[{"LOWER": "virtual"}, {"LOWER": "private"}, {"LOWER": "cloud"}]'),
    ],
    "Amazon Route 53": [
        ("route 53", '[{"LOWER": "route"}, {"LOWER": "53"}]'),
    ],
    "Amazon API Gateway": [
        ("amazon api gateway", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "api"}, {"LOWER": "gateway"}]'),
    ],
    "AWS Direct Connect": [
        ("aws direct connect", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "direct"}, {"LOWER": "connect"}]'),
    ],
    "AWS App Mesh": [
        ("app mesh", '[{"LOWER": "app"}, {"LOWER": "mesh"}]'),
    ],
    "Amazon CloudFront": [
        ("cloudfront", '[{"LOWER": "cloudfront"}]'),
    ],
    "AWS Global Accelerator": [
        ("aws global accelerator", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "global"}, {"LOWER": "accelerator"}]'),
    ],
    "AWS Transit Gateway": [
        ("aws transit gateway", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "transit"}, {"LOWER": "gateway"}]'),
    ],
    "AWS PrivateLink": [
        ("aws privatelink", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "privatelink"}]'),
    ],
    "Amazon Elastic Load Balancing (Amazon ELB)": [
        ("amazon elb", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "elb"}]'),
        ("elastic load balancing", '[{"LOWER": "elastic"}, {"LOWER": "load"}, {"LOWER": "balancing"}]'),
    ],
    "AWS Identity and Access Management (AWS IAM)": [
        ("aws iam", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "iam"}]'),
        ("aws identity and access management", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "identity"}, {"LOWER": "and"}, {"LOWER": "access"}, {"LOWER": "management"}]'),
    ],
    "AWS Organizations": [
        ("aws organizations", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "organizations"}]'),
    ],
    "AWS Certificate Manager (ACM)": [
        ("aws certificate manager", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "certificate"}, {"LOWER": "manager"}]'),
        ("aws acm", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "acm"}]'),
    ],
    "AWS Secrets Manager": [
        ("aws secrets manager", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "secrets"}, {"LOWER": "manager"}]'),
    ],
    "Amazon Web Application Firewall (AWS WAF)": [
        ("aws waf", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "waf"}]'),
        ("aws web application firewall", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "web"}, {"LOWER": "application"}, {"LOWER": "firewall"}]'),
    ],
    "Amazon GuardDuty": [
        ("amazon guardduty", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "guardduty"}]'),
    ],
    "Amazon Macie":[
        ("amazon macie", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "macie"}]'),
    ],
    "AWS Shield": [
        ("aws shield", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "shield"}]'),
    ],
    "AWS Artifact":[
        ("aws artifact", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "artifact"}]'),
    ],
    "AWS Single Sign-On (Amazon SSO)":[
        ("aws sso", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "sso"}]'),
        ("aws single sign-on", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "single"}, {"LOWER": "sign"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "on"}]'),
    ],
    "Amazon Athena":[
        ("amazon athena", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "athena"}]'),
    ],
    "Amazon Elastic MapReduce (Amazon EMR)": [
        ("amazon emr", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "emr"}]'),
        ("amazon elastic mapreduce", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "elastic"}, {"LOWER": "mapreduce"}]'),
        ("amazon elastic map reduce", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "elastic"}, {"LOWER": "map"}, {"LOWER": "reduce"}]'),
    ],
    "Amazon QuickSight":[
        ("quicksight", '[{"LOWER": "quicksight"}]'),
        ("quick sight", '[{"LOWER": "quick"}, {"LOWER": "sight"}]'),
    ],
    "Amazon Kinesis":[
        ("amazon kinesis", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "kinesis"}]'),
    ],
    "AWS Data Pipeline":[
        ("aws data pipeline", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "data"}, {"LOWER": "pipeline"}]'),
    ],
    "AWS Glue": [
        ("aws glue", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "glue"}]'),
    ],
    "AWS Lake Formation": [
        ("aws lake formation", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "lake"}, {"LOWER": "formation"}]'),
    ],
    "Amazon Managed Streaming for Apache Kafka (Amazon MSK)": [
        ("amazon msk", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "msk"}]'),
        ("managed streaming for apache kafka", '[{"LOWER": "managed"}, {"LOWER": "streaming"}, {"LOWER": "for"}, {"LOWER": "apache"}, {"LOWER": "kafka"}]'),
    ],
    "Amazon SageMaker": [
        ("sagemaker", '[{"LOWER": "sagemaker"}]'),
    ],
    "Amazon Comprehend": [
        ("amazon comprehend", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "comprehend"}]'),
    ],
    "Amazon Lex": [
        ("amazon lex", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "lex"}]'),
    ],
    "Amazon Polly":[
        ("amazon polly", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "polly"}]'),
    ],
    "Amazon Rekognition": [
        ("amazon rekognition", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "rekognition"}]'),
    ],
    "Amazon TextTract": [
        ("amazon texttract", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "texttract"}]'),
    ],
    "Amazon Translate": [
        ("amazon translate", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "translate"}]'),
    ],
    "Amazon Transcribe": [
        ("amazon transcribe", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "transcribe"}]'),
    ],
    "AWS DeepRacer": [
        ("aws deepracer", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "deepracer"}]'),
    ],
    "AWS DeepLens": [
        ("aws deeplens", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "deeplens"}]'),
    ],
    "AWS DeepComposer": [
        ("aws deepcomposer", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "deepcomposer"}]'),
    ],
    "Amazon Simple Queue Service (Amazon SQS)": [
        ("amazon sqs", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "sqs"}]'),
        ("amazon simple queue service", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "simple"}, {"LOWER": "queue"}, {"LOWER": "service"}]'),
    ],
    "Amazon Simple Notification Service (Amazon SNS)": [
        ("amazon sns", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "sns"}]'),
        ("amazon simple notification service", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "simple"}, {"LOWER": "notification"}, {"LOWER": "service"}]'),
    ],
    "Amazon EventBridge": [
        ("eventbridge", '[{"LOWER": "eventbridge"}]'),
    ],
    "Amazon AppFlow": [
        ("amazon appflow", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "appflow"}]'),
    ],
    "AWS Step Functions": [
        ("aws step functions", '[,{"LOWER": {"IN": ["aws", "amazon"]} } {"LOWER": "step"}, {"LOWER": "functions"}]'),
    ],
    "AWS Simple Workflow Service (Amazon SWF)": [
        ("aws swf", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "swf"}]'),
        ("aws simple workflow service", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "simple"}, {"LOWER": "workflow"}, {"LOWER": "service"}]'),
    ],
    "Amazon CloudWatch": [
        ("cloudwatch", '[{"LOWER": "cloudwatch"}]'),
    ],
    "AWS Auto Scaling": [
        ("aws auto scaling", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "auto"}, {"LOWER": "scaling"}]'),
    ],
    "AWS CloudFormation": [
        ("cloudformation", '[{"LOWER": "cloudformation"}]'),
    ],
    "AWS CloudTrail": [
        ("cloudtrail", '[{"LOWER": "cloudtrail"}]'),
    ],
    "AWS Config": [
        ("aws config", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "config"}]'),
    ],
    "AWS OpsWorks": [
        ("opsworks", '[{"LOWER": "opsworks"}]'),
    ],
    "AWS Service Catalog": [
        ("aws service catalog", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "service"}, {"LOWER": "catalog"}]'),
    ],
    "AWS Trusted Advisor": [
        ("aws trusted advisor", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "trusted"}, {"LOWER": "advisor"}]'),
    ],
    "AWS Well-Architected Tool": [
        ("aws well-architected tool", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "well"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "architected"}, {"LOWER": "tool"}]'),
    ],
    "AWS Control Tower":[
        ("aws control tower", '[{{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "control"}, {"LOWER": "tower"}]'),
    ],
    "AWS IoT Core": [
        ("aws iot core", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "iot"}, {"LOWER": "core"}]'),
    ],
    "AWS IoT Device Management": [
        ("aws iot device management", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "iot"}, {"LOWER": "device"}, {"LOWER": "management"}]'),
    ],
    "AWS IoT Analytics": [
        ("aws iot analytics", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "iot"}, {"LOWER": "analytics"}]'),
    ],
    "AWS IoT Greengrass": [
        ("aws iot greengrass", '[{"LOWER": {"IN": ["aws", "amazon"]} }, {"LOWER": "iot"}, {"LOWER": "greengrass"}]'),
    ],
    "Waterfall Methodologies": [
        ("waterfall", '[{"LOWER": "waterfall"}]'),
    ],
    "Product Marketing": [
        ("product marketing", '[{"LOWER": "product"}, {"LOWER": "marketing"}]'),
    ],
    "Customer Satisfaction": [
        ("customer satisfaction", '[{"LOWER": "customer"}, {"LOWER": "satisfaction"}]'),
    ],
    "Continuous Improvement": [
        ("continuous improvement", '[{"LOWER": "continuous"}, {"LOWER": "improvement"}]'),
    ],
    "Electrical Engineering": [
        ("electrical engineering", '[{"LOWER": "electrical"}, {"LOWER": "engineering"}]'),
    ],
    "Pre-sales Operations": [
        ("pre-sales", '[{"LOWER": "pre"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "sales"}]'),
    ],
    "Cloud Security": [
        ("cloud security", '[{"LOWER": "cloud"}, {"LOWER": "security"}]'),
    ],
    "Data Security": [
        ("data security", '[{"LOWER": "data"}, {"LOWER": "security"}]'),
    ],
    "Identity and Access Management (IAM)": [
        ("identity and access management", '[{"LOWER": "identity"}, {"LOWER": "and"}, {"LOWER": "access"}, {"LOWER": "management"}]'),
        ("iam", '[{"LOWER": "iam"}]'),
    ],
    "Incident Response": [
        ("incident response", '[{"LOWER": "incident"}, {"LOWER": "response"}]'),
    ],
    "Security Architecture": [
        ("security architecture", '[{"LOWER": "security"}, {"LOWER": "architecture"}]'),
    ],
    "Vulnerability Management": [
        ("vulnerability management", '[{"LOWER": "vulnerability"}, {"LOWER": "management"}]'),
    ],
    "Penetration Testing": [
        ("penetration testing", '[{"LOWER": "penetration"}, {"LOWER": {"IN": ["testing", "test"]} }]'),
    ],
    "Security Awareness and Training": [
        ("security awareness", '[{"LOWER": "security"}, {"LOWER": {"IN": ["awareness", "training", "advocate"]} }]'),
    ],
    "Cryptography": [
        ("cryptography", '[{"LOWER": "cryptography"}]'),
    ],
    "Security Operations": [
        ("security operations", '[{"LOWER": "security"}, {"LOWER": "operations"}]'),
    ],
    "Security Governance and Compliance": [
        ("security governance", '[{"LOWER": "security"}, {"LOWER": {"IN": ["governance", "compliance]} }]'),
    ],
    "Mobile Security": [
        ("mobile security", '[{"LOWER": "mobile"}, {"LOWER": "security"}]'),
    ],
    "Wireless Security": [
        ("wireless security", '[{"LOWER": "wireless"}, {"LOWER": "security"}]'),
    ],
    "Social Engineering": [
        ("social engineering", '[{"LOWER": "social"}, {"LOWER": "engineering"}]'),
    ],
    "Cisco Technologies": [
        ("cisco technologies", '[{"LOWER": "cisco"}, {"LOWER": {"IN": ["technology", "technologies"]} }]'),
    ],
    "Microsoft Exchange": [
        ("microsoft exchange", '[{"LOWER": {"IN": ["ms", "microsoft"]} }, {"LOWER": "exchange"}]'),
    ],
    "Adobe Illustrator": [
        ("adobe illustrator", '[{"LOWER": "adobe"}, {"LOWER": "illustrator"}]'),
    ],
    "Digital Marketing": [
        ("digital marketing", '[{"LOWER": "digital"}, {"LOWER": "marketing"}]'),
    ],
    "Mathematics": [
        ("mathematics", '[{"LOWER": "mathematics"}]'),
    ],
    "Image Processing": [
        ("image processing", '[{"LOWER": "image"}, {"LOWER": "processing"}]'),
    ],
    "XHTML": [
        ("xhtml", '[{"LOWER": "xhtml"}]'),
    ],
    "Financial Analysis": [
        ("financial analysis", '[{"LOWER": "financial"}, {"LOWER": "analysis"}]'),
    ],
    "Six Sigma": [
        ("six sigma", '[{"LOWER": {"IN": ["six", "6"]} }, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "sigma"}]'),
    ],
    "Arduino": [
        ("arduino", '[{"LOWER": "arduino"}]'),
    ],
    "Firebase": [
        ("firebase", '[{"LOWER": "firebase"}]'),
    ],
    "Software Installation": [
        ("software installation", '[{"LOWER": "software"}, {"LOWER": "installation"}]'),
    ],
    "Security Clearance":[
        ("security clearance", '[{"LOWER": "security"}, {"LOWER": "clearance"}]'),
    ],
    "Forecasting": [
        ("forecasting", '[{"LOWER": "forecasting"}]'),
    ],
    "Labview": [
        ("labview", '[{"LOWER": "labview"}]'),
    ],
    "Laravel": [
        ("laravel", '[{"LOWER": "laravel"}]'),
    ],
    "Voice over Internet Protocol (VoIP)": [
        ("voice over internet protocol", '[{"LOWER": "voice"}, {"LOWER": "over"}, {"LOWER": "internet"}, {"LOWER": "protocol"}]'),
        ("voip", '[{"LOWER": "voip"}]'),
    ],
    "Microsoft Power BI": [
        ("power bi", '[{"LOWER": "power"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "bi"}]'),
    ],
    "IBM WebSphere Application Server": [
        ("websphere", '[{"LOWER": "websphere"}]'),
    ],
    "Sales Operations": [
        ("sales operations", '[{"LOWER": "sales"}, {"LOWER": "operations"}]'),
    ],
    "Data Migration": [
        ("data migration", '[{"LOWER": "data"}, {"LOWER": "migration"}]'),
    ],
    "Solution Selling": [
        ("solution selling", '[{"LOWER": "solution"}, {"LOWER": "selling"}]'),
    ],
    "Microsoft Silverlight": [
        ("silverlight", '[{"LOWER": "silverlight"}]'),
    ],
    "Performance Tuning": [
        ("performance tuning", '[{"LOWER": "performance"}, {"LOWER": "tuning"}]'),
    ],
    "Microcontrollers": [
        ("microcontrollers", '[{"LOWER": {"IN": ["microcontrollers", "microcontroller"]} }]'),
    ],
    "Management Consulting": [
        ("management consulting", '[{"LOWER": "management"}, {"LOWER": "consulting"}]'),
    ],
    "Competitive Analysis": [
        ("competitive analysis", '[{"LOWER": "competitive"}, {"LOWER": "analysis"}]'),
    ],
    "Market Research": [
        ("market research", '[{"LOWER": "market"}, {"LOWER": "research"}]'),
    ],
    "ActionScript": [
        ("actionscript", '[{"LOWER": "actionscript"}]'),
        ("action-script", '[{"LOWER": "action"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "script"}]'),
    ],
    "Groovy": [
        ("groovy", '[{"LOWER": "groovy"}]'),
    ],
    "Windows Forms": [
        ("windows forms", '[{"LOWER": "windows"}, {"LOWER": "forms"}]'),
        ("winforms", '[{"LOWER": "winforms"}]'),
    ],
    "Event Management": [
        ("event management", '[{"LOWER": "event"}, {"LOWER": "management"}]'),
    ],
    "Healthcare": [
        ("healthcare", '[{"LOWER": "healthcare"}]'),
    ],
    "Microsoft Visual Basic Scripting Edition (VBScript)": [
        ("vbscript", '[{"LOWER": "vbscript"}]'),
        ("vb-script", '[{"LOWER": "vb"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "script"}]'),
        ("visual basic script", '[{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": {"IN": ["script", "scripting"]} }]'),
    ],
    "Budget Planning": [
        ("budget planning", '[{"LOWER": "budget"}, {"LOWER": "planning"}]'),
        ("budgeting", '[{"LOWER": "budgeting"}]'),
    ],
    "Lean Manufacturing": [
        ("lean manufacturing", '[{"LOWER": "lean"}, {"LOWER": "manufacturing"}]'),
    ],
    "NumPy":[
        ("numpy", '[{"LOWER": "numpy"}]'),
    ],
    "Real-Time Operating System (RTOS)": [
        ("real-time operating system", '[{"LOWER": "real"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "time"}, {"LOWER": "operating"}, {"LOWER": "system"}]'),
        ("rtos", '[{"LOWER": "rtos"}]'),
    ],
    "Bitbucket": [
        ("bitbucket", '[{"LOWER": "bitbucket"}]'),
    ],
    "Assembly Language": [
        ("assembly", '[{"LOWER": "assembly"}]'),
    ],
    "Content Management Systems (CMS)": [
        ("content management system", '[{"LOWER": "content"}, {"LOWER": "management"}, {"LOWER": "system"}]'),
        ("cms", '[{"LOWER": "cms"}]'),
    ],
    "COBOL": [
        ("cobol", '[{"LOWER": "cobol"}]'),
    ],
    "IT Infrastructure": [
        ("infrastructure", '[{"LOWER": "infrastructure"}]'),
    ],
    "Java Persistence API (JPA)": [
        ("jpa", '[{"LOWER": "jpa"}]'),
        ("java persistence api", '[{"LOWER": "java"}, {"LOWER": "persistence"}, {"LOWER": "api"}]'),
    ],
    "Business Planning": [
        ("business planning", '[{"LOWER": "business"}, {"LOWER": "planning"}]'),
    ],
    "Retail": [
        ("retail", '[{"LOWER": "retail"}]'),
    ],
    "Qt (toolkit)": [
        ("qt", '[{"IS_TITLE": true, "LOWER": "qt"}]'),
    ],
    "Drupal": [
        ("drupal", '[{"LOWER": "drupal"}]'),
    ],
    "Finance Understanding": [
        ("finance", '[{"LOWER": "finance"}]'),
    ],
    "Open-source software (OSS)": [
        ("open-source", '[{"LOWER": "open"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "source"}]'),
        ("opensource", '[{"LOWER": "opensource"}]'),
    ],
    "ASP Classic": [
        ("asp", '[{"LOWER": "asp"}, {"LOWER": {"NOT_IN": ["net", ".net", "dotnet", "dot"]} }]'),
    ],
    "Visual Basic for Application (VBA)": [
        ("vba", '[{"LOWER": "vba"}]'),
        ("visual basic for application", '[{"LOWER": "visual"}, {"LOWER": "basic"}, {"LOWER": "for"}, {"LOWER": "application"}]'),
    ],
    "Photography": [
        ("photography", '[{"LOWER": "photography"}]'),
    ],
    "Kanban": [
        ("kanban", '[{"LOWER": "kanban"}]'),
    ],
    "Scripting Language": [
        ("scripting language", '[{"LOWER": "scripting"}, {"LOWER": "language"}]'),
    ],
    "RabbitMQ": [
        ("rabbitmq", '[{"LOWER": "rabbitmq"}]'),
        ("rabbit mq", '[{"LOWER": "rabbit"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "mq"}]'),
    ],
    "Jakarta Enterprise Bean (EJB)": [
        ("ejb", '[{"LOWER": "ejb"}]'),
        ("jakarta enterprise bean", '[{"LOWER": "jakarta"}, {"LOWER": "enterprise"}, {"LOWER": "bean"}]'),
    ],
    "Domain Name System (DNS)": [
        ("dns", '[{"LOWER": "dns"}]'),
        ("domain name system", '[{"LOWER": "domain"}, {"LOWER": "name"}, {"LOWER": "system"}]'),
    ],
    "Accounting": [
        ("accounting", '[{"LOWER": "accounting"}]'),
    ],
    "VHSIC Hardware Description Language (VHDL)": [
        ("vhdl", '[{"LOWER": "vhdl"}]'),
        ("vhsic hardware description language", '[{"LOWER": "vhsic"}, {"LOWER": "hardware"}, {"LOWER": "description"}, {"LOWER": "language"}]'),
    ],
    "Mechanical Engineering": [
        ("mechanical engineering", '[{"LOWER": "mechanical"}, {"LOWER": "engineering"}]'),
    ],
    "Webpack": [
        ("webpack", '[{"LOWER": "webpack"}]'),
    ],
    "Verilog": [
        ("verilog", '[{"LOWER": "verilog"}]'),
    ],
    "Leadership Development": [
        ("leadership development", '[{"LOWER": "leadership"}, {"LOWER": "development"}]'),
    ],
    "IT Operations": [
        ("it operations", '[{"LOWER": "it"}, {"LOWER": "operations"}]'),
    ],
    "Hive": [
        ("hive", '[{"LOWER": "hive"}]'),
    ],
    "Online Marketing": [
        ("online marketing", '[{"LOWER": "online"}, {"LOWER": "marketing"}]'),
    ],
    "Email Marketing": [
        ("email marketing", '[{"LOWER": "email"}, {"LOWER": "marketing"}]'),
    ],
    "Supply Chain Management": [
        ("supply chain management", '[{"LOWER": "supply"}, {"LOWER": "chain"}, {"LOWER": "management"}]'),
    ],
    "Organization Skills": [
        ("organization skills", '[{"LOWER": "organization"}, {"LOWER": "skills"}]'),
    ],
    "Configuration Management": [
        ("configuration management", '[{"LOWER": "configuration"}, {"LOWER": "management"}]'),
    ],
    "Public Relations": [
        ("public relations", '[{"LOWER": "public"}, {"LOWER": "relations"}]'),
    ],
    "Linux, Apache, MySQL, and PHP (LAMP)": [
        ("lamp", '[{"LOWER": "lamp"}]'),
    ],
    "Creative Problem Solving": [
        ("creative problem solving", '[{"LOWER": "creative"}, {"LOWER": "problem"}, {"LOWER": "solving"}]'),
    ],
    "NGINX": [
        ("nginx", '[{"LOWER": "nginx"}]'),
    ],
    "Adobe Flash": [
        ("adobe flash", '[{"LOWER": "adobe"}, {"LOWER": "flash"}]'),
    ],
    "Interpersonal Skills": [
        ("interpersonal skills", '[{"LOWER": "interpersonal"}, {"LOWER": "skills"}]'),
    ],
    "Cucumber": [
        ("cucumber", '[{"LOWER": "cucumber"}]'),
    ],
    "Pandas": [
        ("pandas", '[{"LOWER": "pandas"}]'),
    ],
    "Gradle": [
        ("gradle", '[{"LOWER": "gradle"}]'),
    ],
    "Java Message Service (JMS)": [
        ("jms", '[{"LOWER": "jms"}]'),
        ("java message service", '[{"LOWER": "java"}, {"LOWER": "message"}, {"LOWER": "service"}]'),
    ],
    "System Deployment": [
        ("system deployment", '[{"LOWER": "system"}, {"LOWER": "deployment"}]'),
    ],
    "Microsoft Outlook": [
        ("microsoft outlook", '[{"LOWER": "microsoft"}, {"LOWER": "outlook"}]'),
    ],
    "System Design": [
        ("system design", '[{"LOWER": "system"}, {"LOWER": "design"}]'),
    ],
    "System Applications and Products (SAP)": [
        ("sap", '[{"LOWER": "sap"}]'),
    ],
    "Cloud Applications": [
        ("cloud applications", '[{"LOWER": "cloud"}, {"LOWER": "applications"}]'),
    ],
    "Heroku": [
        ("heroku", '[{"LOWER": "heroku"}]'),
    ],
    "Backbone.JS": [
        ("backbone.js", '[{"LOWER": {"IN": ["backbone.js", "backbonejs"]} }]'),
        ("backbone js", '[{"LOWER": "backbone"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "js"}]'),
    ],
    "Product Design": [
        ("product design", '[{"LOWER": "product"}, {"LOWER": "design"}]'),
    ],
    "Direct Sales": [
        ("direct sales", '[{"LOWER": "direct"}, {"LOWER": "sales"}]'),
    ],
    "Natural Language Processing (NLP)": [
        ("nlp", '[{"LOWER": "nlp"}]'),
        ("natural language processing", '[{"LOWER": "natural"}, {"LOWER": "language"}, {"LOWER": "processing"}]'),
    ],
    "Human Resources (HR)": [
        ("hr", '[{"LOWER": "hr"}]'),
        ("human resources", '[{"LOWER": "human"}, {"LOWER": "resources"}]'),
    ],
    "Project Portfolio Management": [
        ("project portfolio management", '[{"LOWER": "project"}, {"LOWER": "portfolio"}, {"LOWER": "management"}]'),
    ],
    "OpenCV": [
        ("opencv", '[{"LOWER": "opencv"}]'),
    ],
    "Sales Process": [
        ("sales process", '[{"LOWER": "sales"}, {"LOWER": "process"}]'),
    ],
    "Information Assurance": [
        ("information assurance", '[{"LOWER": "information"}, {"LOWER": "assurance"}]'),
    ],
    "Splunk Technology": [
        ("splunk", '[{"LOWER": "splunk"}]'),
    ],
    "Spanish": [
        ("spanish", '[{"LOWER": "spanish"}]'),
    ],
    "NetBeans": [
        ("netbeans", '[{"LOWER": "netbeans"}]'),
    ],
    "Aerospace": [
        ("aerospace", '[{"LOWER": "aerospace"}]'),
    ],
    "Jest": [
        ("jest", '[{"LOWER": "jest"}]'),
    ],
    "Microsoft Visual C++": [
        ("microsoft visual c++", '[{"LOWER": "microsoft"}, {"LOWER": "visual"}, {"LOWER": "c++"}]'),
    ],
    "Postman API": [
        ("postman", '[{"LOWER": "postman"}]'),
    ],
    "Data Engineering": [
        ("data engineering", '[{"LOWER": "data"}, {"LOWER": "engineering"}]'),
    ],
    "Virtual Private Network (VPN)": [
        ("vpn", '[{"LOWER": "vpn"}]'),
        ("virtual private network", '[{"LOWER": "virtual"}, {"LOWER": "private"}, {"LOWER": "network"}]'),
    ],
    "SoapUI": [
        ("soapui", '[{"LOWER": "soapui"}]'),
    ],
    "go-to-market (GTM) strategy": [
        ("go-to-market", '[{"LOWER": "go-to-market"}]'),
        ("gtm", '[{"LOWER": "gtm"}]'),
    ],
    "Test Management": [
        ("test management", '[{"LOWER": "test"}, {"LOWER": "management"}]'),
    ],
    "Contract Management": [
        ("contract management", '[{"LOWER": "contract"}, {"LOWER": "management"}]'),
    ],
    "Presentation Skills": [
        ("presentation skills", '[{"LOWER": "presentation"}, {"LOWER": "skills"}]'),
    ],
    "Blockchain Technology": [
        ("blockchain", '[{"LOWER": "blockchain"}]'),
    ],
    "Concurrent Versioning System (CVS)": [
        ("cvs", '[{"LOWER": "cvs"}]'),
        ("concurrent versioning system", '[{"LOWER": "concurrent"}, {"LOWER": "versioning"}, {"LOWER": "system"}]'),
    ],
    "Adobe InDesign": [
        ("indesign", '[{"LOWER": "indesign"}]'),
    ],
    "Online Advertising": [
        ("online advertising", '[{"LOWER": "online"}, {"LOWER": "advertising"}]'),
    ],
    "Scikit-Learn": [
        ("scikit", '[{"LOWER": "scikit"}]'),
    ],
    "Functional Programming": [
        ("functional programming", '[{"LOWER": "functional"}, {"LOWER": "programming"}]'),
    ],
    "Requirements Management": [
        ("requirements management", '[{"LOWER": "requirements"}, {"LOWER": "management"}]'),
    ],
    "B2B (business-to-business)": [
        ("b2b", '[{"LOWER": "b2b"}]'),
        ("business-to-business", '[{"LOWER": "business"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "to"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "business"}]'),
    ],
    "MapReduce": [
        ("mapreduce", '[{"LOWER": "mapreduce"}]'),
    ],
    "Data Integration": [
        ("data integration", '[{"LOWER": "data"}, {"LOWER": "integration"}]'),
    ],
    "Proposal Writing": [
        ("proposal writing", '[{"LOWER": "proposal"}, {"LOWER": "writing"}]'),
    ],
    "Big Data Analytics": [
        ("big data analytics", '[{"LOWER": "big"}, {"LOWER": "data"}, {"LOWER": "analytics"}]'),
    ],
    "Data Entry": [
        ("data entry", '[{"LOWER": "data"}, {"LOWER": "entry"}]'),
    ],
    "Executive Management": [
        ("executive management", '[{"LOWER": "executive"}, {"LOWER": "management"}]'),
    ],
    "Quality Center": [
        ("quality center", '[{"LOWER": "quality"}, {"LOWER": "center"}]'),
    ],
    "Adobe Dreamweaver": [
        ("dreamweaver", '[{"LOWER": "dreamweaver"}]'),
    ],
    "JavaServer Faces (JSF)": [
        ("jsf", '[{"LOWER": "jsf"}]'),
        ("javaserver faces", '[{"LOWER": "javaserver"}, {"LOWER": "faces"}]'),
    ],
    "Signal Processing": [
        ("signal processing", '[{"LOWER": "signal"}, {"LOWER": "processing"}]'),
    ],
    "Performance Testing": [
        ("performance testing", '[{"LOWER": "performance"}, {"LOWER": "testing"}]'),
    ],
    "Embedded C": [
        ("embedded c", '[{"LOWER": "embedded"}, {"LOWER": "c"}]'),
    ],
    "Project Engineering": [
        ("project engineering", '[{"LOWER": "project"}, {"LOWER": "engineering"}]'),
    ],
    "Marketing Communications": [
        ("marketing communications", '[{"LOWER": "marketing"}, {"LOWER": "communications"}]'),
    ],
    "People Management": [
        ("people management", '[{"LOWER": "people"}, {"LOWER": "management"}]'),
    ],
    "Network Design": [
        ("network design", '[{"LOWER": "network"}, {"LOWER": "design"}]'),
    ],
    "Help Desk Support": [
        ("help desk support", '[{"LOWER": "help"}, {"LOWER": "desk"}, {"LOWER": "support"}]'),
    ],
    "Game Programming": [
        ("game programming", '[{"LOWER": "game"}, {"LOWER": "programming"}]'),
    ],
    "Data Management": [
        ("data management", '[{"LOWER": "data"}, {"LOWER": "management"}]'),
    ],
    "High Availability": [
        ("high availability", '[{"LOWER": "high"}, {"LOWER": "availability"}]'),
    ],
    "Web Analytics": [
        ("web analytics", '[{"LOWER": "web"}, {"LOWER": "analytics"}]'),
    ],
    "Computer-Aided Design (CAD)": [
        ("cad", '[{"LOWER": "cad"}]'),
        ("computer-aided design", '[{"LOWER": "computer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "aided"}, {"LOWER": "design"}]'),
    ],
    "Database Development": [
        ("database development", '[{"LOWER": "database"}, {"LOWER": "development"}]'),
    ],
    "PyTorch": [
        ("pytorch", '[{"LOWER": "pytorch"}]'),
    ],
    "Customer Support": [
        ("customer support", '[{"LOWER": "customer"}, {"LOWER": "support"}]'),
    ],
    "Project Management Office (PMO)": [
        ("pmo", '[{"LOWER": "pmo"}]'),
        ("project management office", '[{"LOWER": "project"}, {"LOWER": "management"}, {"LOWER": "office"}]'),
    ],
    "Network Architecture": [
        ("network architecture", '[{"LOWER": "network"}, {"LOWER": "architecture"}]'),
    ],
    "Physics": [
        ("physics", '[{"LOWER": "physics"}]'),
    ],
    "Wireless Networking": [
        ("wireless networking", '[{"LOWER": "wireless"}, {"LOWER": "networking"}]'),
    ],
    "ArcGIS": [
        ("arcgis", '[{"LOWER": "arcgis"}]'),
    ],
    "Information Architecture": [
        ("information architecture", '[{"LOWER": "information"}, {"LOWER": "architecture"}]'),
    ],
    "Software Implementation": [
        ("software implementation", '[{"LOWER": "software"}, {"LOWER": "implementation"}]'),
    ]
}