import xml.etree.ElementTree as ET

# Contenido XML proporcionado por el usuario (como una cadena de texto)
# En un escenario real, cargarías esto desde un archivo.
xml_data = """
<captiveportal>
	<lan>
		<zone>LAN</zone>
		<descr><![CDATA[servicio de Internet ]]></descr>
		<zoneid>2</zoneid>
		<maxproc></maxproc>
		<timeout></timeout>
		<idletimeout></idletimeout>
		<freelogins_count></freelogins_count>
		<freelogins_resettimeout></freelogins_resettimeout>
		<auth_method>none</auth_method>
		<reauthenticateacct></reauthenticateacct>
		<httpsname></httpsname>
		<preauthurl></preauthurl>
		<blockedmacsurl>https://cliquea.files.wordpress.com/2014/11/conexion.jpg</blockedmacsurl>
		<certref>62a1b161d5740</certref>
		<radius_protocol></radius_protocol>
		<redirurl></redirurl>
		<radiusip></radiusip>
		<radiusip2></radiusip2>
		<radiusip3></radiusip3>
		<radiusip4></radiusip4>
		<radiusport></radiusport>
		<radiusport2></radiusport2>
		<radiusport3></radiusport3>
		<radiusport4></radiusport4>
		<radiusacctport></radiusacctport>
		<radiuskey></radiuskey>
		<radiuskey2></radiuskey2>
		<radiuskey3></radiuskey3>
		<radiuskey4></radiuskey4>
		<radiusvendor>default</radiusvendor>
		<radiussrcip_attribute>wan</radiussrcip_attribute>
		<radmac_format>default</radmac_format>
		<radiusnasid></radiusnasid>
		<page></page>
		<interface>lan</interface>
		<enable></enable>
		<trafficquota></trafficquota>
		<auth_server></auth_server>
		<auth_server2></auth_server2>
		<radacct_server></radacct_server>
		<termsconditions></termsconditions>
		<allowedhostname>
			<hostname>Central-PC</hostname>
			<sn></sn>
			<dir>para </dir>
			<descr><![CDATA[RAUTER DE PRUEBA]]></descr>
			<bw_up>512</bw_up>
			<bw_down>1524</bw_down>
		</allowedhostname>
		<passthrumac>
			<action>pass</action>
			<mac>00:12:33:d1:7f:b1</mac>
			<bw_up>15120</bw_up>
			<bw_down>8200</bw_down>
			<descr><![CDATA[Camara giratoria que se encuentra en el centro de internet suriel con la ip172.16.21.44]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:13:10:96:43:d9</mac>
			<bw_up>3072</bw_up>
			<bw_down>3072</bw_down>
			<descr><![CDATA[#550 Jhonathan Arturo Vinas Ventura Semillero 01 Calle 06 (alante de Arturo) casa 125 día 30 ins 08/03/25 ip 22.250 8299230148]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:5f:67:0e:8b:2b</mac>
			<bw_up>5500</bw_up>
			<bw_down>5500</bw_down>
			<descr><![CDATA[Darling Eduardo Garcia Arias calle 14 semillero 2 edif(al lado de bianca yuderca, edif en construccion, color sapote) 1-1 ins 03/06/25 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:e0:4c:36:05:d8</mac>
			<descr><![CDATA[Celular de santos ip22.100]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:03:01:67</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#372 Emelin Clase San Lorenzo 2 edif 78 1-1 ip22.14 dia 15]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:06:b1:81</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#408 Maria Antonia Capellan Calle 49 c55 Mella 1 8092920955 ins 3/07/23 ip22.63 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:49:9e:81</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[(LEONELDY)Yoel Alvarado calle 1 esquina 12 segundo nivel al lado de la iglesia cienfuegos]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:91:e0:4f</mac>
			<bw_up>8000</bw_up>
			<bw_down>6000</bw_down>
			<descr><![CDATA[#116 Fanny Caraballo Calle 8 Edif. 16 Apto 2-2 Monte Bonito Cienfuegos, 8093092918 (ws)8623060784 (dia 30) ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:91:e0:f5</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#545 Johanna del Carmen Sosa Fondo&nbsp;de&nbsp;Botella Calle 12 Casa 10 Peaton 01 18498894177 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>block</action>
			<mac>00:eb:d8:c4:05:11</mac>
			<bw_up>5500</bw_up>
			<bw_down>5500</bw_down>
			<descr><![CDATA[#489 Francinis Santos Satelite Calle 04 Manzana 22 1-1 (entrando por donde Quivio)Ip22.179 8297038064 ins 18/06/24 dia 30 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>block</action>
			<mac>00:eb:d8:c6:7a:75</mac>
			<bw_up>8000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#318 Yeison Reynoso Almonte calle 3 edif 17 apart 2-1 monte bonito ip134  (dia 15)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7a:85</mac>
			<bw_up>3500</bw_up>
			<bw_down>3500</bw_down>
			<descr><![CDATA[#552 Ana Carela Serv2 CJC Monte Bonito Calle 05 Cafeteria del cjc  ins03/03/25 8297234031 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7a:8f</mac>
			<bw_up>5500</bw_up>
			<bw_down>5500</bw_down>
			<descr><![CDATA[#567 Chaveli Espinal Minaya Monte Bonito Edif 06 Apto 2-3 8299736063 ins 03/05/25 dia 30 pagara 1000]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7a:95</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#496 Victor Jose Colon Alto Bonito Calle 08 Esq 05 829877195 ins 20/07/24 dia 30 ip22.187]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7a:bb</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#338 (Haitiano) Jose Abelo calle 2 c49 (En el Callejon donde Rossanna) San Lorenzo 2 8299451817 ins 23/12/22 ip31.229 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7a:bf</mac>
			<bw_up>6000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#554 Yunilda Altagracia Collado Tejada Calle 29 Casa 14 día 15 ins 14/03/25 8292817901 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7a:f7</mac>
			<bw_up>10100</bw_up>
			<bw_down>10100</bw_down>
			<descr><![CDATA[#46 Mickey Durden Calle 4 San Lorenzo, No. 54 ip22.157 829915188 (dia 20]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:0f</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#280 Mariel Aquino (Madre) Calle 35, con 8 encima de Banca Beco, San Antonio, 8497011721 Inst. 10/12/21  (dia 15)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:15</mac>
			<bw_up>3000</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#502 Veronica Jimenez Satelite Manzana 11 Edif 06 Apto 1-4  8098529361 ins 14/09/24]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:91</mac>
			<bw_up>5400</bw_up>
			<bw_down>8500</bw_down>
			<descr><![CDATA[#17 Adriana Castano Edif. 6 Apto 1-2 8297096541 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:af</mac>
			<bw_up>5100</bw_up>
			<bw_down>8200</bw_down>
			<descr><![CDATA[#551 Jose Arturo Vinas Calle 06 Semillero 01 Casa 109 8299930148 dia 15 ins 08/03/25]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:bd</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#555 Anaury Cristina Vilorio Ramirez La Pina Calle 44 frente al respuesto jonathan de la Pina dia 15 ins 13/03/25 8297664955]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:c7</mac>
			<bw_up>8000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#386 Gysel Altagracia Grullon Calle 12 Casa 12 Fondo de la Botella 8099775964 ip22.37 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:e1</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#494 Katherine De Jesus Calle 2 Valle Bonito Edif 16 Apto c4 82498023316 dia 30 ins 13/07/24 ip22.184]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:c6:7b:e9</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#542 Yasmin Clime Pena Monte Bonito Edif 06 Apto 4-1 8296012236 dia 15]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:cf:93:57</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[(Leoneldy) Ambiorix Taveras colmado Calle 3 con 12 Cienfuegos in22.143 8297077774 ins 24/02/24 dia 3]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>00:eb:d8:f0:6d:61</mac>
			<bw_up>5000</bw_up>
			<bw_down>5000</bw_down>
			<descr><![CDATA[#509 Adriana Emma Balaguer ins 14/10/24 ip22.207]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>04:95:e6:0a:cf:10</mac>
			<bw_up>8000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#381 Yenny Altagracia De La Nuez (Salon) Calle entre calle 18 y 30 caballeros fondo de la botella local 1-1 ins 19/04/23 8092934405 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>04:95:e6:19:a9:60</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#501 Diana Carolina Villalona  Monte Bonito Edif 21 Apto 3-2 18092924064 dia 30 ins 05/09/24 ip21.197]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>04:95:e6:25:d7:40</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#200 Nicol Espinal Henr&iacute;quez (Hermana de Chuky) Calle 12, NO.27 Monte Bonito 8294960765 ip21.48 Inst 21/02/22 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>04:95:e6:78:a7:d0</mac>
			<bw_up>4000</bw_up>
			<bw_down>5000</bw_down>
			<descr><![CDATA[#72 Danilo Sosa (Wanda) Calle 4 No. 22 San Lorenzo 2do Nivel, 8296783854 ip195 (dia 30) ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:0e:3d:8b</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#213 Juana Anyeris Puntiel Semillero 2, Calle 6, No. 10, 8099751418 ip21.68 Inst. 16/03/2022 (dia 20)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:0e:51:71</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#207 Yuleisi Mata De Jimenez Calle 1, c20 8096625892 Inst 5/03/2022 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>block</action>
			<mac>0c:80:63:0e:61:99</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#476 Manuela Maria Reynoso Ozoria San Lorenzo 2 Calle 5 frente a colm Yolanda 2do nivel Apto amarillo dia 30 ip22.155 ins 26/03/24 8299881587]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:0e:62:c9</mac>
			<bw_up>8000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#405 Nurys Jimenez Arnol (Calle Emma Balaguer) edif 21 apart 2-4 monte bonito dia 30 8297487520 ins 21/06/23 ip22.59]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:0e:66:d1</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#548 Ramilito Rodriguez Mena San Antonio Calle 35 8098690467(colmado en la esquina donde vive Wascar y Radeimi) dia 15 ins 15/02/25 pagara 1350 el router es de el ip22.246]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:77:83:f3</mac>
			<bw_up>10200</bw_up>
			<bw_down>10200</bw_down>
			<descr><![CDATA[#537 Maria Magdalena Martines Abre Satelite Manzana 16 Edif 1 Apto 1 Pago. 10 mb. 1500 Va A Pagar La Instalacion El 20/01/2025 Dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:e9:25:8d</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#366 Ligia Elena Melo Guerrero Calle 2 Valle Bonito Edif 7 2,1 8094779848  ins 4/03/23 ip23.5 (dia 15)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:e9:2d:97</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#106 Amartina de Jes&uacute;s Urena Calle 16, Edif. 36, Apto 2-4, Monte Bonito 8297010065 ip 203 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>0c:80:63:e9:9f:69</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#348 Francisca Vicente Pinales casa 07 calle 1ra San Lorenzo 2 dia 15 ip20.135 8297032045 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>10:7d:1a:2f:1f:46</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[Madelin Luciano]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>14:91:82:f3:fa:eb</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#114 Juliana Pena Calle 5, No. 38, ensanche San Lorenzo 2, 8498040173 ip213 (dia 30) ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:16:e7</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#397 Celeste Tejada San Lorenzo 2 Calle 7 Casa 5 8298040651 ip22.49 ins 27/05/23 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:18:7b</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#480 Clarissa Pina Nunez San Antonio Calle 27, No 05 dia 15 ins 19/03/24 ip22.55]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:18:c3</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#398 David Rogriguez San Lorenzo 2 Calle 5 Apto 3-1 (Edif Yasmin) 8296248258 15 ins 27/05/33 ip22.50]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:1e:f1</mac>
			<bw_up>5500</bw_up>
			<bw_down>7000</bw_down>
			<descr><![CDATA[#425 Fernanda Aquino Baez Mella 1 Edif 1 Apto 2-3 entre calle 27 y 61 (segun edenorte) 8499178214 ip21.86 dia 15 ins 20/09/23 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:20:d7</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#523 Sandra Ayala Semillero 2 Calle 06 Casa 70 ins 23/11/24 ip22.218]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:23:9f</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#411 Veronica Isabel Cruz Semillero 2 Calle 9 c35 colegio Ridea  8296101519  ins 18/07/23 ip22.68 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:24:09</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#384 Raydiris Cabrera Martinez Monte Bonito Edif 13 Apto 3-1 8092838135 ins 22/04/23 ip22.28 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:24:3d</mac>
			<bw_up>5500</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#95 Ramon Mora Calle 04, No. 33 8295481361 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:24:65</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#229 Albanelis Rodriguez Valle bonito, Calle 1, No. 32, (parque) 8293386255 Inst. 7/03/22 ip21.59 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:29:09</mac>
			<bw_up>8100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#166 Mireya Francisca Alto Bonito, Calle 8, No. 154, 8296609141 ip182 Inst. 27/11/21 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:2a:2b</mac>
			<bw_up>5100</bw_up>
			<bw_down>6500</bw_down>
			<descr><![CDATA[#361 Eridania Silverio Moronta calle 2 manzana 11 edif 4 apart 1-2 (Satelite Corriente) 8295180075  ip20.99 ins 18/02/23 (dia 15)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:2a:81</mac>
			<bw_up>5500</bw_up>
			<bw_down>5500</bw_down>
			<descr><![CDATA[(SA)Pedro Ezequiel Lopez Peralta calle 6 con 14 semillero (edenorte dice edif  3) 2 apart 2-1 8296907820 dia 30 ins 27/04/24 ip22.165 pagara 1100]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:2c:1b</mac>
			<bw_up>6000</bw_up>
			<bw_down>7500</bw_down>
			<descr><![CDATA[#562 Ricardo Martinez Martinez Calle 35 Casa 32 ins 07/04/25 8496202665 ip21.47 dia 30 pagara 800 y debe 800 de instalacion que la pagara el proximo mes]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:2f:01</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#471 Albairis Rodriguez Calle 01 Casa 32 Valle Bonito ins 5/03/24 (Al lado de Albanelis) 8493770387 ip22.148]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:34:6d</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#481 Luis David Morla Serv2 calle 2 valle bonito edif 30 apart 1-1 (La baarberia) 8294481205 pagara 800 el proximo 30 de 30/04/24 dia 30 ins 15/04/24 ip22.162]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:1e:34:8b</mac>
			<bw_up>8100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#390 Wanda Maciel Marte Calle 12 Casa 9 (Al lado de rosaslinda) ip22.41 ins 9/05/23 8293914771  1150 (dia 30) ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>1c:3b:f3:3d:ca:6d</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#430 Rodolfo Gonzales San Lorenzo 2 Calle 39 Casa 6 (En la calle que vive Hensly martinez casa que queda al final de la calle la ultima) 8293706786 dia 30 ins 28/10/23 ip22.94]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>28:ee:52:b4:d3:07</mac>
			<bw_up>5350</bw_up>
			<bw_down>5200</bw_down>
			<descr><![CDATA[#212 Jean Marco Ruth Peralta El Semillero 2, Calle 6, No. 55, ip21.66 8095060276  Inst. 14/03/22 (dia 15)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:ca:29</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#498 Esperanza de la Cruz San Lorenzo 2 Esq 04 (al lado de la tienda la casa verde que está atras del solar) Casa 29 2do nivel dia 15 ins 14/08/24 8496514270 ip22.190]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:ca:2f</mac>
			<bw_up>100000</bw_up>
			<bw_down>100000</bw_down>
			<descr><![CDATA[leoneldy emergencia]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d2:f1</mac>
			<bw_up>6000</bw_up>
			<bw_down>6000</bw_down>
			<descr><![CDATA[#536 Malvin Aneudis Ferreira Gil Satelite Manzana 11 Edif 08 Apto 2 8297316633 Plan 5 mb 1000 Dia 15 ins 11/01/25 ip22.231]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d3:31</mac>
			<bw_up>5100</bw_up>
			<bw_down>7000</bw_down>
			<descr><![CDATA[#221 Luisa Andreina Cabrera Ventura ip165 Monte Bonito Edif 11 Apto 4-3 8095104445 Inst 2/04/2022 (dia 5)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d3:47</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#549 Starling Rodriguez  Barrio Alegria Calle 59 Casa ( el no sabe pero es azul con blanco y tiene una marquesina) dia 30 ins 07/03/25 ip22.249 8295228895]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d3:55</mac>
			<bw_up>11500</bw_up>
			<bw_down>11500</bw_down>
			<descr><![CDATA[#556 Jorge Luis Contreras Ensanche Almarosa 1 Seco 1 Calle 09 Casa 02 dia 30 ins 11/03/25 8093183619]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d3:8f</mac>
			<bw_up>12000</bw_up>
			<bw_down>12000</bw_down>
			<descr><![CDATA[#156 Hensly Martinez Calle 39 c52 8494571212  ins 17/11/2021 ip55 (dia 20)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d3:97</mac>
			<bw_up>10000</bw_up>
			<bw_down>10000</bw_down>
			<descr><![CDATA[Centro de Internet]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d3:cf</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#303 Mariela Zapata Calle 4 c31 San Lorenzo 2 8296926092 ip21.182 ins 4/10/22 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:03</mac>
			<bw_up>6000</bw_up>
			<bw_down>6000</bw_down>
			<descr><![CDATA[new #60 Yahaira Mej&iacute;a Edif 13 Apto 2-4 Monte Bonito 8299182999 ip231 (dia 20) ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:33</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#510 Angela Genao Fondo de Botella Calle 15 Casa 13 ins 09/10/24 dia 30 ip22.205]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:67</mac>
			<bw_up>5120</bw_up>
			<bw_down>5120</bw_down>
			<descr><![CDATA[(LEONELDY) Dilenny Lisbeth]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:71</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#530 Jessi Diaz Calle 01 Valle Bonito Casa 08 (frente a Albairis) 8498829766 ins 02/12/24 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>block</action>
			<mac>30:16:9d:0d:d4:73</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#532 Jorge Miguel Sanchez Semillero 2 Calle 15 3-3 (subiendo la 5 cerca del colmadon por el colmadon) dia 30 8097146345 ins 28/12/24 ip22.227]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:91</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#493 Ana Felicia Hernandez Monte Bonito Edif 16 Apto 4-2 dia 30 ins 01/07/24 8293997659 22.183]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:97</mac>
			<bw_up>3200</bw_up>
			<bw_down>3200</bw_down>
			<descr><![CDATA[#510 Orquidea De La Cruz Martinez Semillero 2 Calle 06 Casa 76 2-1(encima de Manuel sadan) 8494370404 dia 15 ins 10/10/24]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:a9</mac>
			<bw_up>5100</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#160 Johanna Jim&eacute;nez, Calle, 35 c19 San Antonio 8295803999  ip53 ins 19/11/21 (dia 20)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d4:cd</mac>
			<bw_up>6000</bw_up>
			<bw_down>6000</bw_down>
			<descr><![CDATA[#557 Jeffry Manuel Martinez Mella 1, Calle Neno, Edif 04 Apto 1-6 el Ultimo dia 30 ints 26/02/2025ip 22.247]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d5:23</mac>
			<bw_up>3000</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#499 Margarita Luna Monte Bonito Edif 11 Apto 4-4 encima de la junta dia 15 Ins 14/08/24 ip22.191 8098043731]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d5:c1</mac>
			<bw_up>8000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[Cliente leoneldy]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d5:cd</mac>
			<bw_up>5000</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#506 Ernesto Rodriguez San Lorenzo 2 Calle 02 Edif Apto 02 (al lado de la iglesia)  8294596555 dia 30 ins 24/09/24]]></descr>
		</passthrumac>
		<passthrumac>
			<action>block</action>
			<mac>30:16:9d:0d:d5:d5</mac>
			<bw_up>5500</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#517 Crisaidy Guerrero Valle Bonito Calle 02 Edif 32 Puerta 07 8295091840 ins 04/11/24 8295091840 ins 04/11/24 dia 15 ip22.212]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:3d</mac>
			<bw_up>5500</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#491 Eddy Manuel Montero de Leon Valle Bonito Calle 02 Edif 16 Apto 10 (2do nivel) 8492053852 ins 29/06/24 dia 15 ip21.181]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:41</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#547 Michael De Lo Santo Hernandez calle Valle bonito (justamente al lado de jennifer en el apartamento mamei, el dice que no tiene nombre) dia 30 ip22.2244 ins 12/02/2025]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:53</mac>
			<bw_up>5500</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#495 Adonis Rodriguez El Ollo Calle 31 Casa 106 Iglesia  dia 30 ins 16/07/24 8097907561 (serv puede ser a nombre de Wascar) ip22.186]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:61</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#10 Mirian Cabrera Edif 7, 1-4, (dia 10)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:69</mac>
			<bw_up>5500</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#497 Elvin Ozoria Monte Bonito Edif 36 Apto 2-2 8094858772 ins 25/07/24 dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:73</mac>
			<bw_up>8500</bw_up>
			<bw_down>8500</bw_down>
			<descr><![CDATA[#162 Francia Hernandez Garcia Edif 22 2-2 monte bonito ip54 ins 20/12/2021 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:75</mac>
			<bw_up>8000</bw_up>
			<bw_down>10000</bw_down>
			<descr><![CDATA[#539 Fiordaliza Quiroz Monte Bonito Calle 16 Edif 11 Apto 2-3 ins 11/01/25 dia 15 8099686707 ip22.234]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:91</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#541 Danibel Nunez Valdez Fondo de Botella Calle 13 Casa No Sabe, es en la calle donde vive Britany sosa, justamente al lado en la casa de color azul con blanco y hirrros negros) ins 15/01/25 dia 15 8296915541 ip22.237]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d6:97</mac>
			<bw_up>4000</bw_up>
			<bw_down>4000</bw_down>
			<descr><![CDATA[#544 Will Antonio Urena Sanchez Edif 07 Apto 2-2 8098683062 pagara 500 dice leoneldy ins 31/01/24 dia 30 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:21</mac>
			<bw_up>5500</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#559 Jose Daniel Infante Rodriguez San Antonio Calle 2 Edif Apto 9c mamei donde vive Sindy Burgos día 15 829 455 8928 ip20.85 ins 24/03/25 pagara 1,000]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:2b</mac>
			<bw_up>7300</bw_up>
			<bw_down>7300</bw_down>
			<descr><![CDATA[#563 Lismayri Hernandez Fondo de Botella Calle 15 casa justamente frente al caritas(ella no sabe nada mas de su ubicacion pero esto es un Apto que tiene como parque o frente a caritas fondo de botella) 8297686927 ins 11/04/24 dia 30 ip22.193]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:33</mac>
			<bw_up>11000</bw_up>
			<bw_down>11000</bw_down>
			<descr><![CDATA[#564 Esmerlin Contrera (hablar con el para datos) 8092932536 ins 20/03/25]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:a5</mac>
			<bw_up>6500</bw_up>
			<bw_down>6500</bw_down>
			<descr><![CDATA[#466 Pedro Pichardo Satelite Manzana 15 Edif 2 Apto 2-2 ins 20/02/24 8092528485 satelite dia 30 ip22.129]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:bd</mac>
			<bw_up>3071</bw_up>
			<bw_down>3071</bw_down>
			<descr><![CDATA[LEO Damari Rodriguez Cienfuegos Calle 01 Casa 73 Parte Atras (mama de mujer Aneury)dia 30 8292634347 ins 09/11/24]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:cd</mac>
			<bw_up>6000</bw_up>
			<bw_down>6000</bw_down>
			<descr><![CDATA[#553 Olga Maria Payams Rodriguez Barrio Alegria Calle 55 Casa (no se sabe) por el play 8293102981 dia 30 ins 15/03/25 20.132]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:d3</mac>
			<bw_up>5100</bw_up>
			<bw_down>11000</bw_down>
			<descr><![CDATA[#535 Rosmely Mercado San Antonio Calle 29 Casa 61 dia 30 ins 04/01/24 8099019755 ip22.228]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d7:e9</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#534 Darleny Yohanna Vasquez Fondo de Botella Calle 15 2do Nivel frente a la fotografa yokaty (ella no sabe el numero de edif ni apto 8297907524 dia 30) ins 05/01/25 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d8:2b</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#513 Michael Olivo Camilo Cruz San Antonio Calle 31 Casa 36 (frente a Edinson De Leon cabrera) ins 16/10/24 ip 22.208  8622153684 dia 15]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d8:df</mac>
			<bw_up>5000</bw_up>
			<bw_down>8100</bw_down>
			<descr><![CDATA[#422 Josefa Polano Calle 1 (arriba del colmado catalina ella no se sabe el numero) casa azul segundo nivel (La mamá de Albania) ins 4/09/23 ip22.82  8299136156 (dia 30)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d8:f5</mac>
			<bw_up>10500</bw_up>
			<bw_down>10500</bw_down>
			<descr><![CDATA[#450 Anderson Jackson (MIllonario) San Lorenzo 2 Calle 8 con 4 8099076165 (Encima del colmado apart 11 ultimo piso, No hay muchos detalles acerca de esa ubicacion) dia 30]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d9:03</mac>
			<bw_up>5100</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#528 Estarlin Rodriguez Serv2 San Lorenzo Calle 04 Casa 31 (entrar por el callejon que esta al lado de Mariela Zapata y frente al colmado 8297680123 dia 15 ip22.222 ins 02/12/24]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d9:0d</mac>
			<bw_up>7300</bw_up>
			<bw_down>8000</bw_down>
			<descr><![CDATA[#546 Victor Pizarro Calle 25 Esq 27 Valle Bonito Casa 48 dia 30 ins 03/01/25 ip22.243]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d9:23</mac>
			<bw_up>15000</bw_up>
			<bw_down>15000</bw_down>
			<descr><![CDATA[#543 Orquidea Martinez Semillero 01 Calle 07 Casa 08 parte atrás Cienfuegos 8299056214 dia 15 ins 24/01/25]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>30:16:9d:0d:d9:8b</mac>
			<bw_up>4022</bw_up>
			<bw_down>4022</bw_down>
			<descr><![CDATA[#514 Aurelio Acevedo Calle 14 Esq 05 Apto 132 2-03(el no esta seguro, encima del repuesto de la calle 5 por el 20 y10 cuando subes al 2do nivel la 1ra puerta que vez, exactamente debajo de la escalera el cable de internet entra por la ventana que esta serca de la escalera es en el 2do nivel) dia 15 ins 17/10/24 8096052053 ip22.209]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>34:e8:94:87:d1:85</mac>
			<bw_up>3072</bw_up>
			<bw_down>3072</bw_down>
			<descr><![CDATA[(SA)Manaury Riveron Pena Mella 1 calle 37 edif 37 2-6 dia 30 ins 30/04/24 ip22.164 8295856885]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>38:6b:1c:0a:5b:23</mac>
			<bw_up>3100</bw_up>
			<bw_down>6000</bw_down>
			<descr><![CDATA[#34 Otoniel Cordero Calle 5 (dia 15)]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>38:6b:1c:13:a8:01</mac>
			<bw_up>5100</bw_up>
			<bw_down>5100</bw_down>
			<descr><![CDATA[#511 Albania Polanco Servicio 2 Calle 01 Esq 7 local 11 (En el salon 8099836148 ip22.169 ins 04/05/24 dia 15 ]]></descr>
		</passthrumac>
		<passthrumac>
			<action>pass</action>
			<mac>38:6b:1c:27:d9:ab</mac>
			<bw_up>8300</bw_up>
			<bw_down>8300</bw_down>
			
		</passthrumac>
	</lan>
</captiveportal>
"""

# Convertir Kbps a Mbps para los umbrales
UMBRAL_10_MBPS_KBPS = 10000  # 10 Mbps = 10,000 Kbps
UMBRAL_50_MBPS_KBPS = 50000  # 50 Mbps = 50,000 Kbps

# Listas para almacenar los resultados
clientes_mas_de_10_mbps = []
clientes_mas_de_50_mbps = []
clientes_sin_bw = []

try:
    # Cargar el XML desde la cadena de texto
    root = ET.fromstring(xml_data)

    # Si el XML estuviera en un archivo (por ejemplo, 'pfsense_config.xml'),
    # lo cargarías así:
    # tree = ET.parse('pfsense_config.xml')
    # root = tree.getroot()

    # Buscar todas las entradas 'passthrumac' dentro de 'captiveportal/lan'
    # También buscamos en 'allowedhostname' por si acaso, aunque en tu ejemplo solo 'passthrumac' tiene los bw_
    for entry in root.findall('.//passthrumac') + root.findall('.//allowedhostname'):
        mac = entry.find('mac')
        # Para allowedhostname, el MAC se puede encontrar en 'hostname' o similar si no hay 'mac' tag.
        # En tu ejemplo, allowedhostname tiene 'hostname' en lugar de 'mac'
        # Ajustamos para que busque 'hostname' si 'mac' no está presente
        if mac is None:
            mac_or_id = entry.find('hostname')
            if mac_or_id is not None:
                mac_or_id = mac_or_id.text
            else:
                mac_or_id = "Desconocido (No MAC/Hostname)" # Fallback si no hay identificador
        else:
            mac_or_id = mac.text

        bw_up_elem = entry.find('bw_up')
        bw_down_elem = entry.find('bw_down')
        descr_elem = entry.find('descr')

        bw_up = None
        bw_down = None
        descr = "Sin descripción"

        if descr_elem is not None and descr_elem.text:
            descr = descr_elem.text.strip()

        if bw_up_elem is not None and bw_up_elem.text:
            try:
                bw_up = int(bw_up_elem.text)
            except ValueError:
                bw_up = None # No es un número válido

        if bw_down_elem is not None and bw_down_elem.text:
            try:
                bw_down = int(bw_down_elem.text)
            except ValueError:
                bw_down = None # No es un número válido

        # Lógica de filtrado
        if bw_up is None and bw_down is None:
            clientes_sin_bw.append({
                "MAC/ID": mac_or_id,
                "Descripción": descr
            })
        else:
            # Comprobar si supera los 10 Mbps
            if (bw_up is not None and bw_up >= UMBRAL_10_MBPS_KBPS) or \
               (bw_down is not None and bw_down >= UMBRAL_10_MBPS_KBPS):
                clientes_mas_de_10_mbps.append({
                    "MAC/ID": mac_or_id,
                    "Subida (Kbps)": bw_up,
                    "Bajada (Kbps)": bw_down,
                    "Descripción": descr
                })

            # Comprobar si supera los 50 Mbps
            if (bw_up is not None and bw_up >= UMBRAL_50_MBPS_KBPS) or \
               (bw_down is not None and bw_down >= UMBRAL_50_MBPS_KBPS):
                clientes_mas_de_50_mbps.append({
                    "MAC/ID": mac_or_id,
                    "Subida (Kbps)": bw_up,
                    "Bajada (Kbps)": bw_down,
                    "Descripción": descr
                })

except ET.ParseError as e:
    print(f"Error al analizar el XML: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# --- Imprimir resultados ---

print("--- Clientes con Ancho de Banda > 10 Mbps ---")
if clientes_mas_de_10_mbps:
    for cliente in clientes_mas_de_10_mbps:
        print(f"MAC/ID: {cliente['MAC/ID']}")
        print(f"  Subida: {cliente['Subida (Kbps)']} Kbps ({cliente['Subida (Kbps)']/1000:.2f} Mbps)")
        print(f"  Bajada: {cliente['Bajada (Kbps)']} Kbps ({cliente['Bajada (Kbps)']/1000:.2f} Mbps)")
        print(f"  Descripción: {cliente['Descripción']}")
        print("-" * 30)
else:
    print("No se encontraron clientes con más de 10 Mbps.")

print("\n--- Clientes con Ancho de Banda > 50 Mbps ---")
if clientes_mas_de_50_mbps:
    for cliente in clientes_mas_de_50_mbps:
        print(f"MAC/ID: {cliente['MAC/ID']}")
        print(f"  Subida: {cliente['Subida (Kbps)']} Kbps ({cliente['Subida (Kbps)']/1000:.2f} Mbps)")
        print(f"  Bajada: {cliente['Bajada (Kbps)']} Kbps ({cliente['Bajada (Kbps)']/1000:.2f} Mbps)")
        print(f"  Descripción: {cliente['Descripción']}")
        print("-" * 30)
else:
    print("No se encontraron clientes con más de 50 Mbps.")

print("\n--- Clientes sin Ancho de Banda Asignado (Libres) ---")
if clientes_sin_bw:
    for cliente in clientes_sin_bw:
        print(f"MAC/ID: {cliente['MAC/ID']}")
        print(f"  Descripción: {cliente['Descripción']}")
        print("-" * 30)
else:
    print("No se encontraron clientes sin ancho de banda asignado.")