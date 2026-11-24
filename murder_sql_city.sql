-- murder en sql city
-- 15 de enero de 2018  


-- 1) SELECT * FROM crime_scene_report
--    WHERE type = "murder" and city = "SQL City" and date = 20180115 

--> date	type	description	city
--> 20180115	murder	Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". 
-- Las grabaciones de seguridad muestran que había dos testigos. El primer testigo vive en la última casa de "Northwestern Dr". 
-- La segunda testigo, llamada Annabel, vive en algún lugar de "Franklin Ave".


-------- PRIMER TESTIGO --------------------------------------

-- 2) SELECT * FROM person 
--    WHERE address_street_name LIKE "Northwestern Dr" 


-- 3) SELECT * FROM person 
--    WHERE address_street_name LIKE "Northwestern Dr"
--    ORDER BY adress_number DESC LIMIT 1

-- id	    name	        license_id  address_number	address_street_name	ssn
-- 14887	Morty Schapiro	118009	    4919	        Northwestern Dr	
-- #PRIMER TESTIGO


-- 4) SELECT * FROM interview
--    WHERE person_id LIKE "14887"

-- Escuché un disparo y luego vi a un hombre salir corriendo. Llevaba una bolsa del gimnasio "Get Fit Now". 
-- El número de socio en la bolsa comenzaba con "48Z". Solo los socios Gold tienen esas bolsas. 
-- El hombre se subió a un coche con una matrícula que incluía "H42W".


-- 5) SELECT * FROM get_fit_now_member
--    WHERE id LIKE "48Z%" and membership_status = "gold";

-- id	    person_id	name	        membership_start_date	membership_status
-- 48Z7A	28819	    Joe Germuska	20160305	            gold
-- 48Z55	67318	    Jeremy Bowers	20160101	            gold


-- 6) SELECT * FROM drivers_license
--    WHERE plate_number LIKE "H42W%"

-- id	    age	height	eye_color	hair_color	gender	plate_number	car_make	car_model
-- 183779	21	65	    blue	    blonde	    female	H42W0X	        Toyota	    Prius


-- 7) SELECT * FROM interview
--    WHERE person_id LIKE "67318"

-- Me contrató una mujer con mucho dinero. No sé su nombre, pero sé que mide alrededor de 1,65 m (65") o 1,70 m (67"). 
-- Tiene el pelo rojo y conduce un Tesla Model S. Sé que asistió al concierto de la Orquesta Sinfónica de SQL tres veces en diciembre de 2017.


-- select * from drivers_license
-- where car_model like "model s"

-- id	    age	height	eye_color	hair_color	gender	plate_number	car_make	car_model
-- 918773	48	65	    black	    red	        female	917UU3	        Tesla	    Model S
-- 202298	68	66	    green	    red	        female	500123	        Tesla	    Model S
-- 291182	65	66	    blue	    red	        female	08CM64	        Tesla	    Model S

-- select * from person
-- where license_id like "202298"

-- id	    name	            license_id	address_number	address_street_name	ssn
-- 99716	Miranda Priestly	202298	    1883	        Golden Ave	        987756388


-- select * from facebook_event_checkin
-- where person_id like "99716"


------------------------- SEGUNDO TESTIGO --------------------

-- 8) select * from person
--    where address_street_name like "franklin ave"

-- id	    name	            license_id	    address_number	address_street_name	ssn
-- 16371	Annabel Miller	    490173	        103	            Franklin Ave	    318771143
-- SEGUNDO TESTIGO


-- 9) select * from interview
--    where person_id like "16371"

-- Presencié el asesinato y reconocí al asesino del gimnasio donde entrenaba la semana pasada, el 9 de enero.

-- 10) select * from get_fit_now_check_in
--     where check_in_date like "20180109"


