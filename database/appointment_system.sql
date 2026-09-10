--
-- PostgreSQL database dump
--

\restrict IpjnLLKvitAya0QbsO4xxepzmfNTsUH4LpCdQnTeplR7hKW3Y5Y0UfYD33i1heI

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-09-08 23:42:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 16552)
-- Name: appointments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.appointments (
    id integer NOT NULL,
    professional_id integer NOT NULL,
    client_id integer NOT NULL,
    datetime_slot timestamp without time zone NOT NULL,
    state character varying(20) NOT NULL,
    duration integer NOT NULL
);


ALTER TABLE public.appointments OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16551)
-- Name: appointments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.appointments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.appointments_id_seq OWNER TO postgres;

--
-- TOC entry 5048 (class 0 OID 0)
-- Dependencies: 225
-- Name: appointments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.appointments_id_seq OWNED BY public.appointments.id;


--
-- TOC entry 220 (class 1259 OID 16515)
-- Name: clients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clients (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(200) NOT NULL,
    phone character varying(50)
);


ALTER TABLE public.clients OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16514)
-- Name: clients_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clients_id_seq OWNER TO postgres;

--
-- TOC entry 5049 (class 0 OID 0)
-- Dependencies: 219
-- Name: clients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clients_id_seq OWNED BY public.clients.id;


--
-- TOC entry 222 (class 1259 OID 16525)
-- Name: professionals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professionals (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    specialty character varying(100) NOT NULL,
    default_duration_minutes integer NOT NULL
);


ALTER TABLE public.professionals OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16524)
-- Name: professionals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.professionals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.professionals_id_seq OWNER TO postgres;

--
-- TOC entry 5050 (class 0 OID 0)
-- Dependencies: 221
-- Name: professionals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.professionals_id_seq OWNED BY public.professionals.id;


--
-- TOC entry 224 (class 1259 OID 16536)
-- Name: working_hours; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.working_hours (
    id integer NOT NULL,
    professional_id integer NOT NULL,
    day_of_week character varying(20) NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL
);


ALTER TABLE public.working_hours OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16535)
-- Name: working_hours_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.working_hours_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.working_hours_id_seq OWNER TO postgres;

--
-- TOC entry 5051 (class 0 OID 0)
-- Dependencies: 223
-- Name: working_hours_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.working_hours_id_seq OWNED BY public.working_hours.id;


--
-- TOC entry 4874 (class 2604 OID 16555)
-- Name: appointments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appointments ALTER COLUMN id SET DEFAULT nextval('public.appointments_id_seq'::regclass);


--
-- TOC entry 4871 (class 2604 OID 16518)
-- Name: clients id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);


--
-- TOC entry 4872 (class 2604 OID 16528)
-- Name: professionals id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professionals ALTER COLUMN id SET DEFAULT nextval('public.professionals_id_seq'::regclass);


--
-- TOC entry 4873 (class 2604 OID 16539)
-- Name: working_hours id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.working_hours ALTER COLUMN id SET DEFAULT nextval('public.working_hours_id_seq'::regclass);


--
-- TOC entry 5042 (class 0 OID 16552)
-- Dependencies: 226
-- Data for Name: appointments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.appointments (id, professional_id, client_id, datetime_slot, state, duration) FROM stdin;
149	229	204	2026-05-18 10:00:00	pending	30
152	235	209	2026-05-18 10:00:00	pending	30
159	247	218	2026-08-31 10:00:00	confirmed	30
155	241	213	2026-05-18 10:00:00	canceled	30
160	248	220	2026-05-18 10:00:00	pending	30
164	254	225	2026-05-18 10:00:00	pending	30
168	260	231	2026-08-31 10:00:00	confirmed	30
169	260	231	2026-08-31 11:00:00	canceled	30
170	261	232	2026-05-18 10:00:00	pending	30
174	267	237	2026-05-18 10:00:00	pending	30
178	273	242	2026-05-18 10:00:00	pending	30
182	26	191	2026-09-14 17:00:00	pending	30
183	279	247	2026-05-18 10:00:00	pending	30
187	285	252	2026-09-14 17:00:00	confirmed	60
188	26	191	2026-09-14 16:00:00	canceled	30
189	286	253	2026-05-18 10:00:00	pending	30
193	292	259	2026-09-14 17:00:00	confirmed	60
148	218	195	2026-05-18 10:00:00	canceled	30
\.


--
-- TOC entry 5036 (class 0 OID 16515)
-- Dependencies: 220
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clients (id, name, email, phone) FROM stdin;
191	Juan Perez	juan.perez@gmail.com	1123456789
193	Juan Perez	juan.nuevo@gmail.com	1123456789
195	Test Client	test@example.com	\N
199	Juan Perez	juan@gmail.com	123456789
204	Test Client	test_ad5c11f3-fa8f-486c-bd7a-30d40d1b1cc6@example.com	\N
209	Test Client	test_3d529b24-e7d1-4a02-ae37-bb6ecfb5e610@example.com	\N
213	Test Client	test_9c3b3c3f-c58d-4f1b-b768-ff6a3de076b4@example.com	\N
218	Lucas Gonzalez	lucas.gonzalez@gmail.com	1123456789
220	Test Client	test_9b1a1a96-425b-40b9-a77e-b3ab9c083d6a@example.com	\N
225	Test Client	test_b53affef-bd4a-4534-a0cf-2c68278f0fa8@example.com	\N
231	Juan Perez	juanperez@gmail.com	1123456789
232	Test Client	test_76a4b15f-54c9-4cde-b2c3-eacc84d98d28@example.com	\N
237	Test Client	test_b85e171d-9b62-418d-a4dd-666efb80efdd@example.com	\N
242	Test Client	test_c1e6faeb-79fe-49a6-b9a7-8be6679d98b6@example.com	\N
247	Test Client	test_734fdfd0-ec38-4eb8-8672-d5d5430c2b57@example.com	\N
252	Juan Pérez	juan.perez@test.com	1123456789
253	Test Client	test_457602d0-6e34-4496-a6d3-3cc26e1cc9e3@example.com	\N
259	Juan Perez	juan.perez2@gmail.com	1123456789
\.


--
-- TOC entry 5038 (class 0 OID 16525)
-- Dependencies: 222
-- Data for Name: professionals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professionals (id, name, specialty, default_duration_minutes) FROM stdin;
2	Test	General	30
3	Test	General	30
4	Test	General	30
5	Test	General	30
6	Test	General	30
7	Test	General	30
8	Test	General	30
9	Test	General	30
10	Test	General	30
11	Test	General	30
12	Test	General	30
13	Test	General	30
14	Test	General	30
15	Test	General	30
16	Test	General	30
17	Test	General	30
18	Test	General	30
19	Test	General	30
20	Test	General	30
21	Test	General	30
22	Test	General	30
23	Test	General	30
24	Test	General	30
25	Test	General	30
26	Test	General	30
27	Test	General	30
28	Test	General	30
29	Test	General	30
30	Test	General	30
31	Test	General	30
32	Test	General	30
33	Test	General	30
34	Test	General	30
35	Test	General	30
36	Test	General	30
37	Test	General	30
38	Test	General	30
39	Test	General	30
40	Test	General	30
41	Test	General	30
42	Test	General	30
43	Test	General	30
44	Test	General	30
45	Test	General	30
46	Test	General	30
47	Test	General	30
48	Test	General	30
49	Test	General	30
50	Test	General	30
51	Test	General	30
52	Test	General	30
53	Test	General	30
54	Test	General	30
55	Test	General	30
56	Test	General	30
57	Test	General	30
58	Test	General	30
59	Test	General	30
60	Test	General	30
61	Test	General	30
62	Test	General	30
63	Test	General	30
64	Test	General	30
65	Test	General	30
66	Test	General	30
67	Test	General	30
68	Test	General	30
70	Test	General	30
71	Test	General	30
72	Test	General	30
73	Dr. Juan Pérez	Dermatology	30
74	Test	General	30
75	Test	General	30
76	Test	General	30
77	Dr. Juan Pérez	Dermatology	30
78	Test	General	30
79	Test	General	30
80	Test	General	30
81	Dr. Juan Pérez	Dermatology	30
82	Test	General	30
83	Test	General	30
84	Test	General	30
85	Dr. Juan Pérez	Dermatology	30
86	Test	General	30
87	Test	General	30
88	Test	General	30
89	Dr. Juan Pérez	Dermatology	30
90	Test	General	30
91	Test	General	30
92	Test	General	30
93	Dr. Juan Pérez	Dermatology	30
94	Test	General	30
95	Test	General	30
96	Test	General	30
97	Dr. Juan Pérez	Dermatology	30
98	Test	General	30
99	Test	General	30
100	Test	General	30
101	Dr. Juan Pérez	Dermatology	30
102	Test	General	30
103	Test	General	30
104	Test	General	30
105	Dr. Juan Pérez	Dermatology	30
106	Test	General	30
107	Test	General	30
108	Test	General	30
109	Dr. Juan Pérez	Dermatology	30
110	Test	General	30
111	Test	General	30
112	Test	General	30
113	Dr. Juan Pérez	Dermatology	30
114	Test	General	30
115	Test	General	30
116	Test	General	30
117	Dr. Juan Pérez	Dermatology	30
118	Test	General	30
119	Test	General	30
120	Test	General	30
121	Dr. Juan Pérez	Dermatology	30
122	Test	Cardiologia	30
123	Test	Cardiologia	30
124	Test	General	30
125	Test	General	30
126	Test	General	30
127	Dr. Juan Pérez	Dermatology	30
128	Test	Cardiologia	30
129	Test	Cardiologia	30
130	Test	General	30
131	Test	General	30
132	Test	General	30
133	Dr. Juan Pérez	Dermatology	30
134	Test	Cardiologia	30
135	Test	Cardiologia	30
136	Juan Perez	Cardiologia	30
137	Juan Perez	Cardiologia	30
138	Maria Gomez	Dermatologia	45
139	Test	General	30
140	Test	General	30
141	Test	General	30
142	Dr. Juan Pérez	Dermatology	30
143	Test	Cardiologia	30
144	Test	Cardiologia	30
145	Test	General	30
146	Test	General	30
147	Test	General	30
148	Dr. Juan Pérez	Dermatology	30
149	Test	Cardiologia	30
150	Test	Cardiologia	30
151	Test	General	30
152	Test	General	30
153	Test	General	30
154	Dr. Juan Pérez	Dermatology	30
155	Test	Cardiologia	30
156	Test	Cardiologia	30
157	Test	General	30
158	Test	General	30
159	Test	General	30
160	Dr. Juan Pérez	Dermatology	30
161	Test	Cardiologia	30
162	Test	Cardiologia	30
163	Test	General	30
164	Test	General	30
165	Test	General	30
166	Dr. Juan Pérez	Dermatology	30
167	Test	Cardiologia	30
168	Test	Cardiologia	30
169	Test	General	30
170	Test	General	30
171	Test	General	30
172	Dr. Juan Pérez	Dermatology	30
173	Test	Cardiologia	30
174	Test	Cardiologia	30
175	Test	General	30
176	Test	General	30
177	Test	General	30
178	Dr. Juan Pérez	Dermatology	30
179	Test	Cardiologia	30
180	Test	Cardiologia	30
181	Test	General	30
182	Test	General	30
183	Test	General	30
184	Dr. Juan Pérez	Dermatology	30
185	Test	Cardiologia	30
186	Test	Cardiologia	30
187	Test	General	30
188	Test	General	30
189	Test	General	30
190	Dr. Juan Pérez	Dermatology	30
191	Test	Cardiologia	30
192	Test	Cardiologia	30
193	Test	General	30
194	Test	General	30
195	Test	General	30
196	Dr. Juan Pérez	Dermatology	30
197	Test	Cardiologia	30
198	Test	Cardiologia	30
199	Test	General	30
200	Test	General	30
201	Test	General	30
202	Dr. Juan Pérez	Dermatology	30
203	Test	Cardiologia	30
204	Test	Cardiologia	30
205	Test	General	30
206	Test	General	30
207	Test	General	30
208	Dr. Juan Pérez	Dermatology	30
209	Test	Cardiologia	30
210	Test	Cardiologia	30
211	Test	General	30
212	Test	General	30
213	Test	General	30
214	Dr. Juan Pérez	Dermatology	30
215	Test	Cardiologia	30
216	Test	Cardiologia	30
217	Carlos Rodriguez	string	30
218	Test	General	30
219	Test	General	30
220	Test	General	30
221	Dr. Juan Pérez	Dermatology	30
222	Test	Cardiologia	30
223	Test	Cardiologia	30
226	Dr. Juan Pérez	Dermatology	30
227	Test	Cardiologia	30
228	Test	Cardiologia	30
229	Test	General	30
232	Dr. Juan Pérez	Dermatology	30
233	Test	Cardiologia	30
234	Test	Cardiologia	30
235	Test	General	30
238	Dr. Juan Pérez	Dermatology	30
239	Test	Cardiologia	30
240	Test	Cardiologia	30
241	Test	General	30
244	Dr. Juan Pérez	Dermatology	30
245	Test	Cardiologia	30
246	Test	Cardiologia	30
247	Dr. Juan Perez	Cardiologia	30
248	Test	General	30
251	Dr. Juan Pérez	Dermatology	30
252	Test	Cardiologia	30
253	Test	Cardiologia	30
254	Test	General	30
257	Dr. Juan Pérez	Dermatology	30
258	Test	Cardiologia	30
259	Test	Cardiologia	30
260	Dr. Carlos Gomez	Cardiologia	30
261	Test	General	30
264	Dr. Juan Pérez	Dermatology	30
265	Test	Cardiologia	30
266	Test	Cardiologia	30
267	Test	General	30
270	Dr. Juan Pérez	Dermatology	30
271	Test	Cardiologia	30
272	Test	Cardiologia	30
273	Test	General	30
276	Dr. Juan Pérez	Dermatology	30
277	Test	Cardiologia	30
278	Test	Cardiologia	30
279	Test	General	30
282	Dr. Juan Pérez	Dermatology	30
283	Test	Cardiologia	30
284	Test	Cardiologia	30
285	Dr. Test	string	60
286	Test	General	30
289	Dr. Juan Pérez	Dermatology	30
290	Test	Cardiologia	30
291	Test	Cardiologia	30
292	Dr. Carlos Gomez	Kinesiología	60
\.


--
-- TOC entry 5040 (class 0 OID 16536)
-- Dependencies: 224
-- Data for Name: working_hours; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.working_hours (id, professional_id, day_of_week, start_time, end_time) FROM stdin;
1	26	Lunes	09:00:00	18:00:00
2	29	Lunes	09:00:00	18:00:00
3	32	Lunes	09:00:00	18:00:00
4	35	Lunes	09:00:00	18:00:00
5	38	Lunes	09:00:00	18:00:00
6	41	Lunes	09:00:00	18:00:00
7	44	Lunes	09:00:00	18:00:00
8	47	Lunes	09:00:00	18:00:00
9	50	Lunes	09:00:00	18:00:00
10	53	Lunes	09:00:00	18:00:00
11	56	Lunes	09:00:00	18:00:00
12	59	Lunes	09:00:00	18:00:00
13	62	Lunes	09:00:00	18:00:00
14	65	Lunes	09:00:00	18:00:00
15	68	Lunes	09:00:00	18:00:00
16	72	Lunes	09:00:00	18:00:00
17	73	Lunes	09:00:00	12:00:00
18	73	Lunes	14:00:00	18:00:00
19	73	Martes	09:00:00	13:00:00
20	73	Miercoles	10:00:00	16:00:00
21	76	Lunes	09:00:00	18:00:00
22	77	Lunes	09:00:00	12:00:00
23	77	Lunes	14:00:00	18:00:00
24	77	Martes	09:00:00	13:00:00
25	77	Miercoles	10:00:00	16:00:00
26	80	Lunes	09:00:00	18:00:00
27	81	Lunes	09:00:00	12:00:00
28	81	Lunes	14:00:00	18:00:00
29	81	Martes	09:00:00	13:00:00
30	81	Miercoles	10:00:00	16:00:00
31	85	Lunes	09:00:00	12:00:00
32	85	Lunes	14:00:00	18:00:00
33	85	Martes	09:00:00	13:00:00
34	85	Miercoles	10:00:00	16:00:00
35	89	Lunes	09:00:00	12:00:00
36	89	Lunes	14:00:00	18:00:00
37	89	Martes	09:00:00	13:00:00
38	89	Miercoles	10:00:00	16:00:00
39	93	Lunes	09:00:00	12:00:00
40	93	Lunes	14:00:00	18:00:00
41	93	Martes	09:00:00	13:00:00
42	93	Miercoles	10:00:00	16:00:00
43	97	Lunes	09:00:00	12:00:00
44	97	Lunes	14:00:00	18:00:00
45	97	Martes	09:00:00	13:00:00
46	97	Miercoles	10:00:00	16:00:00
47	101	Lunes	09:00:00	12:00:00
48	101	Lunes	14:00:00	18:00:00
49	101	Martes	09:00:00	13:00:00
50	101	Miercoles	10:00:00	16:00:00
51	105	Lunes	09:00:00	12:00:00
52	105	Lunes	14:00:00	18:00:00
53	105	Martes	09:00:00	13:00:00
54	105	Miercoles	10:00:00	16:00:00
55	109	Lunes	09:00:00	12:00:00
56	109	Lunes	14:00:00	18:00:00
57	109	Martes	09:00:00	13:00:00
58	109	Miercoles	10:00:00	16:00:00
59	113	Lunes	09:00:00	12:00:00
60	113	Lunes	14:00:00	18:00:00
61	113	Martes	09:00:00	13:00:00
62	113	Miercoles	10:00:00	16:00:00
63	117	Lunes	09:00:00	12:00:00
64	117	Lunes	14:00:00	18:00:00
65	117	Martes	09:00:00	13:00:00
66	117	Miercoles	10:00:00	16:00:00
67	121	Lunes	09:00:00	12:00:00
68	121	Lunes	14:00:00	18:00:00
69	121	Martes	09:00:00	13:00:00
70	121	Miercoles	10:00:00	16:00:00
71	122	Lunes	09:00:00	17:00:00
72	123	Lunes	09:00:00	17:00:00
73	127	Lunes	09:00:00	12:00:00
74	127	Lunes	14:00:00	18:00:00
75	127	Martes	09:00:00	13:00:00
76	127	Miercoles	10:00:00	16:00:00
77	128	Lunes	09:00:00	17:00:00
78	129	Lunes	09:00:00	17:00:00
79	133	Lunes	09:00:00	12:00:00
80	133	Lunes	14:00:00	18:00:00
81	133	Martes	09:00:00	13:00:00
82	133	Miercoles	10:00:00	16:00:00
83	134	Lunes	09:00:00	17:00:00
84	135	Lunes	09:00:00	17:00:00
85	136	Lunes	09:00:00	17:00:00
86	137	Lunes	09:00:00	17:00:00
87	138	Lunes	09:00:00	13:00:00
88	138	Miercoles	14:00:00	18:00:00
89	142	Lunes	09:00:00	12:00:00
90	142	Lunes	14:00:00	18:00:00
91	142	Martes	09:00:00	13:00:00
92	142	Miercoles	10:00:00	16:00:00
93	143	Lunes	09:00:00	17:00:00
94	144	Lunes	09:00:00	17:00:00
95	148	Lunes	09:00:00	12:00:00
96	148	Lunes	14:00:00	18:00:00
97	148	Martes	09:00:00	13:00:00
98	148	Miercoles	10:00:00	16:00:00
99	149	Lunes	09:00:00	17:00:00
100	150	Lunes	09:00:00	17:00:00
101	154	Lunes	09:00:00	12:00:00
102	154	Lunes	14:00:00	18:00:00
103	154	Martes	09:00:00	13:00:00
104	154	Miercoles	10:00:00	16:00:00
105	155	Lunes	09:00:00	17:00:00
106	156	Lunes	09:00:00	17:00:00
107	160	Lunes	09:00:00	12:00:00
108	160	Lunes	14:00:00	18:00:00
109	160	Martes	09:00:00	13:00:00
110	160	Miercoles	10:00:00	16:00:00
111	161	Lunes	09:00:00	17:00:00
112	162	Lunes	09:00:00	17:00:00
113	166	Lunes	09:00:00	12:00:00
114	166	Lunes	14:00:00	18:00:00
115	166	Martes	09:00:00	13:00:00
116	166	Miercoles	10:00:00	16:00:00
117	167	Lunes	09:00:00	17:00:00
118	168	Lunes	09:00:00	17:00:00
119	172	Lunes	09:00:00	12:00:00
120	172	Lunes	14:00:00	18:00:00
121	172	Martes	09:00:00	13:00:00
122	172	Miercoles	10:00:00	16:00:00
123	173	Lunes	09:00:00	17:00:00
124	174	Lunes	09:00:00	17:00:00
125	178	Lunes	09:00:00	12:00:00
126	178	Lunes	14:00:00	18:00:00
127	178	Martes	09:00:00	13:00:00
128	178	Miercoles	10:00:00	16:00:00
129	179	Lunes	09:00:00	17:00:00
130	180	Lunes	09:00:00	17:00:00
131	184	Lunes	09:00:00	12:00:00
132	184	Lunes	14:00:00	18:00:00
133	184	Martes	09:00:00	13:00:00
134	184	Miercoles	10:00:00	16:00:00
135	185	Lunes	09:00:00	17:00:00
136	186	Lunes	09:00:00	17:00:00
137	190	Lunes	09:00:00	12:00:00
138	190	Lunes	14:00:00	18:00:00
139	190	Martes	09:00:00	13:00:00
140	190	Miercoles	10:00:00	16:00:00
141	191	Lunes	09:00:00	17:00:00
142	192	Lunes	09:00:00	17:00:00
143	196	Lunes	09:00:00	12:00:00
144	196	Lunes	14:00:00	18:00:00
145	196	Martes	09:00:00	13:00:00
146	196	Miercoles	10:00:00	16:00:00
147	197	Lunes	09:00:00	17:00:00
148	198	Lunes	09:00:00	17:00:00
149	202	Lunes	09:00:00	12:00:00
150	202	Lunes	14:00:00	18:00:00
151	202	Martes	09:00:00	13:00:00
152	202	Miercoles	10:00:00	16:00:00
153	203	Lunes	09:00:00	17:00:00
154	204	Lunes	09:00:00	17:00:00
155	208	Lunes	09:00:00	12:00:00
156	208	Lunes	14:00:00	18:00:00
157	208	Martes	09:00:00	13:00:00
158	208	Miercoles	10:00:00	16:00:00
159	209	Lunes	09:00:00	17:00:00
160	210	Lunes	09:00:00	17:00:00
161	214	Lunes	09:00:00	12:00:00
162	214	Lunes	14:00:00	18:00:00
163	214	Martes	09:00:00	13:00:00
164	214	Miercoles	10:00:00	16:00:00
165	215	Lunes	09:00:00	17:00:00
166	216	Lunes	09:00:00	17:00:00
167	217	Lunes	09:00:00	13:00:00
168	217	Lunes	14:00:00	18:00:00
169	217	Martes	09:00:00	13:00:00
170	221	Lunes	09:00:00	12:00:00
171	221	Lunes	14:00:00	18:00:00
172	221	Martes	09:00:00	13:00:00
173	221	Miercoles	10:00:00	16:00:00
174	222	Lunes	09:00:00	17:00:00
175	223	Lunes	09:00:00	17:00:00
176	226	Lunes	09:00:00	12:00:00
177	226	Lunes	14:00:00	18:00:00
178	226	Martes	09:00:00	13:00:00
179	226	Miercoles	10:00:00	16:00:00
180	227	Lunes	09:00:00	17:00:00
181	228	Lunes	09:00:00	17:00:00
182	232	Lunes	09:00:00	12:00:00
183	232	Lunes	14:00:00	18:00:00
184	232	Martes	09:00:00	13:00:00
185	232	Miercoles	10:00:00	16:00:00
186	233	Lunes	09:00:00	17:00:00
187	234	Lunes	09:00:00	17:00:00
188	238	Lunes	09:00:00	12:00:00
189	238	Lunes	14:00:00	18:00:00
190	238	Martes	09:00:00	13:00:00
191	238	Miercoles	10:00:00	16:00:00
192	239	Lunes	09:00:00	17:00:00
193	240	Lunes	09:00:00	17:00:00
194	244	Lunes	09:00:00	12:00:00
195	244	Lunes	14:00:00	18:00:00
196	244	Martes	09:00:00	13:00:00
197	244	Miercoles	10:00:00	16:00:00
198	245	Lunes	09:00:00	17:00:00
199	246	Lunes	09:00:00	17:00:00
200	247	Lunes	09:00:00	13:00:00
201	247	Lunes	14:00:00	18:00:00
202	247	Martes	09:00:00	13:00:00
203	247	Miercoles	10:00:00	16:00:00
204	251	Lunes	09:00:00	12:00:00
205	251	Lunes	14:00:00	18:00:00
206	251	Martes	09:00:00	13:00:00
207	251	Miercoles	10:00:00	16:00:00
208	252	Lunes	09:00:00	17:00:00
209	253	Lunes	09:00:00	17:00:00
210	257	Lunes	09:00:00	12:00:00
211	257	Lunes	14:00:00	18:00:00
212	257	Martes	09:00:00	13:00:00
213	257	Miercoles	10:00:00	16:00:00
214	258	Lunes	09:00:00	17:00:00
215	259	Lunes	09:00:00	17:00:00
216	260	Lunes	09:00:00	13:00:00
217	260	Lunes	14:00:00	18:00:00
218	260	Martes	09:00:00	13:00:00
219	264	Lunes	09:00:00	12:00:00
220	264	Lunes	14:00:00	18:00:00
221	264	Martes	09:00:00	13:00:00
222	264	Miercoles	10:00:00	16:00:00
223	265	Lunes	09:00:00	17:00:00
224	266	Lunes	09:00:00	17:00:00
225	270	Lunes	09:00:00	12:00:00
226	270	Lunes	14:00:00	18:00:00
227	270	Martes	09:00:00	13:00:00
228	270	Miercoles	10:00:00	16:00:00
229	271	Lunes	09:00:00	17:00:00
230	272	Lunes	09:00:00	17:00:00
231	276	Lunes	09:00:00	12:00:00
232	276	Lunes	14:00:00	18:00:00
233	276	Martes	09:00:00	13:00:00
234	276	Miercoles	10:00:00	16:00:00
235	277	Lunes	09:00:00	17:00:00
236	278	Lunes	09:00:00	17:00:00
237	282	Lunes	09:00:00	12:00:00
238	282	Lunes	14:00:00	18:00:00
239	282	Martes	09:00:00	13:00:00
240	282	Miercoles	10:00:00	16:00:00
241	283	Lunes	09:00:00	17:00:00
242	284	Lunes	09:00:00	17:00:00
243	285	Lunes	09:00:00	18:00:00
244	289	Lunes	09:00:00	12:00:00
245	289	Lunes	14:00:00	18:00:00
246	289	Martes	09:00:00	13:00:00
247	289	Miercoles	10:00:00	16:00:00
248	290	Lunes	09:00:00	17:00:00
249	291	Lunes	09:00:00	17:00:00
250	292	Lunes	09:00:00	18:00:00
\.


--
-- TOC entry 5052 (class 0 OID 0)
-- Dependencies: 225
-- Name: appointments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.appointments_id_seq', 193, true);


--
-- TOC entry 5053 (class 0 OID 0)
-- Dependencies: 219
-- Name: clients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clients_id_seq', 259, true);


--
-- TOC entry 5054 (class 0 OID 0)
-- Dependencies: 221
-- Name: professionals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.professionals_id_seq', 292, true);


--
-- TOC entry 5055 (class 0 OID 0)
-- Dependencies: 223
-- Name: working_hours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.working_hours_id_seq', 250, true);


-- Completed on 2026-09-08 23:42:26

--
-- PostgreSQL database dump complete
--

\unrestrict IpjnLLKvitAya0QbsO4xxepzmfNTsUH4LpCdQnTeplR7hKW3Y5Y0UfYD33i1heI

