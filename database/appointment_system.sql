-- ============================================================
-- Appointment System
-- Database initialization script
-- ============================================================

-- ============================================================
-- TABLES
-- ============================================================

CREATE TABLE public.clients (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(200) NOT NULL,
    phone character varying(50)
);

CREATE TABLE public.professionals (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    specialty character varying(100) NOT NULL,
    default_duration_minutes integer NOT NULL
);

CREATE TABLE public.working_hours (
    id integer NOT NULL,
    professional_id integer NOT NULL,
    day_of_week character varying(20) NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL
);

CREATE TABLE public.appointments (
    id integer NOT NULL,
    professional_id integer NOT NULL,
    client_id integer NOT NULL,
    datetime_slot timestamp without time zone NOT NULL,
    state character varying(20) NOT NULL,
    duration integer NOT NULL
);

-- ============================================================
-- SEQUENCES
-- ============================================================

CREATE SEQUENCE public.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.professionals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.working_hours_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.appointments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

-- ============================================================
-- DEFAULT VALUES
-- ============================================================

ALTER TABLE ONLY public.clients
    ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);

ALTER TABLE ONLY public.professionals
    ALTER COLUMN id SET DEFAULT nextval('public.professionals_id_seq'::regclass);

ALTER TABLE ONLY public.working_hours
    ALTER COLUMN id SET DEFAULT nextval('public.working_hours_id_seq'::regclass);

ALTER TABLE ONLY public.appointments
    ALTER COLUMN id SET DEFAULT nextval('public.appointments_id_seq'::regclass);

-- ============================================================
-- CLIENTS
-- ============================================================

INSERT INTO public.clients (id, name, email, phone) VALUES
(1, 'Santiago Lopez', 'santiago.lopez@gmail.com', '1123456789'),
(2, 'Camila Fernandez', 'camila.fernandez@gmail.com', '1134567890'),
(3, 'Mateo Gonzalez', 'mateo.gonzalez@gmail.com', '1145678901'),
(4, 'Valentina Rodriguez', 'valentina.rodriguez@gmail.com', '1156789012'),
(5, 'Lucas Martinez', 'lucas.martinez@gmail.com', '1167890123'),
(6, 'Sofia Perez', 'sofia.perez@gmail.com', '1178901234'),
(7, 'Martin Alvarez', 'martin.alvarez@gmail.com', '1189012345'),
(8, 'Julieta Romero', 'julieta.romero@gmail.com', '1190123456'),
(9, 'Nicolas Torres', 'nicolas.torres@gmail.com', '1101234567'),
(10, 'Agustina Diaz', 'agustina.diaz@gmail.com', '1112345678'),
(11, 'Tomas Sosa', 'tomas.sosa@gmail.com', '1123456790'),
(12, 'Florencia Castro', 'florencia.castro@gmail.com', '1134567801'),
(13, 'Federico Ruiz', 'federico.ruiz@gmail.com', '1145678012'),
(14, 'Mariana Silva', 'mariana.silva@gmail.com', '1156789123'),
(15, 'Benjamin Acosta', 'benjamin.acosta@gmail.com', '1167890234');

-- ============================================================
-- PROFESSIONALS
-- ============================================================

INSERT INTO public.professionals (
    id,
    name,
    specialty,
    default_duration_minutes
) VALUES
(1, 'Laura Martinez', 'Psicologia', 60),
(2, 'Martin Rodriguez', 'Clinica Medica', 30),
(3, 'Sofia Fernandez', 'Nutricion', 45),
(4, 'Diego Gonzalez', 'Kinesiologia', 45),
(5, 'Valentina Perez', 'Dermatologia', 30);

-- ============================================================
-- WORKING HOURS
-- ============================================================

INSERT INTO public.working_hours (
    id,
    professional_id,
    day_of_week,
    start_time,
    end_time
) VALUES

-- Laura Martinez - Psicologia
(1, 1, 'Lunes', '09:00:00', '13:00:00'),
(2, 1, 'Miércoles', '14:00:00', '19:00:00'),
(3, 1, 'Viernes', '09:00:00', '13:00:00'),

-- Martin Rodriguez - Clinica Medica
(4, 2, 'Lunes', '08:00:00', '12:00:00'),
(5, 2, 'Martes', '14:00:00', '18:00:00'),
(6, 2, 'Jueves', '08:00:00', '12:00:00'),

-- Sofia Fernandez - Nutricion
(7, 3, 'Martes', '09:00:00', '13:00:00'),
(8, 3, 'Jueves', '15:00:00', '19:00:00'),
(9, 3, 'Viernes', '09:00:00', '13:00:00'),

-- Diego Gonzalez - Kinesiologia
(10, 4, 'Lunes', '14:00:00', '18:00:00'),
(11, 4, 'Miércoles', '09:00:00', '13:00:00'),
(12, 4, 'Viernes', '14:00:00', '18:00:00'),

-- Valentina Perez - Dermatologia
(13, 5, 'Martes', '09:00:00', '13:00:00'),
(14, 5, 'Miércoles', '14:00:00', '18:00:00'),
(15, 5, 'Jueves', '09:00:00', '13:00:00');

-- ============================================================
-- APPOINTMENTS
-- ============================================================

INSERT INTO public.appointments (
    id,
    professional_id,
    client_id,
    datetime_slot,
    state,
    duration
) VALUES

-- Laura Martinez
(1, 1, 1, '2026-09-07 10:00:00', 'confirmed', 60),
(2, 1, 2, '2026-09-07 11:00:00', 'pending', 60),
(3, 1, 3, '2026-09-09 15:00:00', 'confirmed', 60),
(4, 1, 4, '2026-09-14 14:00:00', 'pending', 60),
(5, 1, 5, '2026-09-16 16:00:00', 'confirmed', 60),

-- Martin Rodriguez
(6, 2, 6, '2026-09-07 09:00:00', 'confirmed', 30),
(7, 2, 7, '2026-09-08 15:00:00', 'pending', 30),
(8, 2, 8, '2026-09-08 15:30:00', 'confirmed', 30),
(9, 2, 9, '2026-09-14 08:30:00', 'confirmed', 30),
(10, 2, 10, '2026-09-15 16:00:00', 'pending', 30),

-- Sofia Fernandez
(11, 3, 11, '2026-09-08 10:00:00', 'confirmed', 45),
(12, 3, 12, '2026-09-10 16:00:00', 'pending', 45),
(13, 3, 13, '2026-09-11 10:00:00', 'confirmed', 45),
(14, 3, 14, '2026-09-15 09:00:00', 'pending', 45),
(15, 3, 15, '2026-09-17 17:00:00', 'confirmed', 45),

-- Diego Gonzalez
(16, 4, 1, '2026-09-07 15:00:00', 'confirmed', 45),
(17, 4, 2, '2026-09-09 10:00:00', 'pending', 45),
(18, 4, 3, '2026-09-11 15:00:00', 'confirmed', 45),
(19, 4, 4, '2026-09-14 16:00:00', 'pending', 45),
(20, 4, 5, '2026-09-18 14:00:00', 'confirmed', 45),

-- Valentina Perez
(21, 5, 6, '2026-09-08 09:30:00', 'confirmed', 30),
(22, 5, 7, '2026-09-09 15:00:00', 'pending', 30),
(23, 5, 8, '2026-09-10 10:00:00', 'confirmed', 30),
(24, 5, 9, '2026-09-15 11:00:00', 'pending', 30),
(25, 5, 10, '2026-09-17 09:30:00', 'canceled', 30);

-- ============================================================
-- UPDATE SEQUENCES
-- ============================================================

SELECT pg_catalog.setval(
    'public.clients_id_seq',
    15,
    true
);

SELECT pg_catalog.setval(
    'public.professionals_id_seq',
    5,
    true
);

SELECT pg_catalog.setval(
    'public.working_hours_id_seq',
    15,
    true
);

SELECT pg_catalog.setval(
    'public.appointments_id_seq',
    25,
    true
);

