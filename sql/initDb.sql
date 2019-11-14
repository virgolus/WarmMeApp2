CREATE USER 'warmme'@'%' IDENTIFIED BY 'warmme';
CREATE DATABASE warmme;

create table activation_status
(
    zone_id     int                                 not null,
    created     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    state       varchar(11) collate utf8_unicode_ci null,
    temperature float                               null
);

create table activation_status_current
(
    zone_id     int                                 not null,
    created     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    state       varchar(11) collate utf8_unicode_ci null,
    temperature float                               null
);

create table activation_target
(
    id      int auto_increment
        primary key,
    created timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    type    varchar(60)                         null,
    zone_id int                                 not null
)
    collate = utf8_unicode_ci;

create table activation_target_manual
(
    id          int auto_increment
        primary key,
    created     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    temperature float                               null,
    zone_id     int                                 not null
)
    collate = utf8_unicode_ci;

create table activation_target_schedule
(
    id          int auto_increment
        primary key,
    schedule_id int   not null,
    startTime   time  not null,
    endTime     time  not null,
    temperature float not null
);

create table schedule
(
    id      int auto_increment
        primary key,
    zone_id int          null,
    name    varchar(100) null
);

create table sensor
(
    id      int auto_increment
        primary key,
    zone_id int                                 not null,
    type    varchar(100)                        not null,
    name    varchar(60) collate utf8_unicode_ci not null,
    uuid    varchar(100)                        null
);

create table sensor_monitor
(
    id          int auto_increment
        primary key,
    sensor_id   int                                 not null,
    created     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    temperature float                               not null,
    humidity    float                               not null
);

create table sensor_monitor_last
(
    id          int auto_increment
        primary key,
    sensor_id   int                                 not null,
    created     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    temperature float                               not null,
    humidity    float                               not null
);

create table sensor_parameter
(
    id          int auto_increment
        primary key,
    sensor_id   int                          not null,
    name        text collate utf8_unicode_ci not null,
    description text collate utf8_unicode_ci null,
    value       text collate utf8_unicode_ci not null
);

create table zone
(
    id   int auto_increment
        primary key,
    name varchar(200) not null
);

create table activator
(
    id   int auto_increment
        primary key,
    zone_id   int                          not null,
    name        text collate utf8_unicode_ci not null,
    description text collate utf8_unicode_ci null,
    gpio_pin   int                          not null
);

-- Insert
INSERT INTO activation_status (zone_id, created, state, temperature) VALUES (1, '2019-11-13 13:19:50', 'OFF', 23);
INSERT INTO activation_status_current (zone_id, created, state, temperature) VALUES (1, '2019-11-13 13:19:50', 'OFF', 23);
INSERT INTO activation_manual (id, created, temperature, zone_id) VALUES (1, '2015-01-31 22:24:20', 21.1, 1);
INSERT INTO activation_schedule (id, schedule_id, startTime, endTime, temperature) VALUES (1, 1, '06:45:00', '07:30:00', 20);
INSERT INTO activation_schedule (id, schedule_id, startTime, endTime, temperature) VALUES (2, 1, '18:00:00', '23:59:00', 21);
INSERT INTO activation_target (id, created, type, zone_id) VALUES (1, '2015-02-01 17:34:00', 'MANUAL', 1);
INSERT INTO sensor_monitor_last (id, sensor_id, created, temperature, humidity) VALUES (1, 1, '2015-02-01 18:05:17', 20.625, 0);
INSERT INTO sensor_monitor (id, sensor_id, created, temperature, humidity) VALUES (1, 1, '2015-02-01 18:05:17', 20.625, 0);
INSERT INTO sensor_parameter (id, sensor_id, name, description, value) VALUES (1, 1, 'TempCorrectionValue', 'Correction value for temperature sensor', '0');
INSERT INTO sensor_parameter (id, sensor_id, name, description, value) VALUES (3, 1, 'ConnectionPinNumber', '', '4');
INSERT INTO sensor_parameter (id, sensor_id, name, description, value) VALUES (4, 1, 'DHTType', '', '22');
INSERT INTO sensor (id, zone_id, type, name, uuid) VALUES (1, 1, 'DaveTheBraveSensor', 'Temperature sensor 01', null);
INSERT INTO zone (id, name) VALUES (1, 'Zona giorno');
INSERT INTO zone (id, name) VALUES (2, 'Zona notte');
INSERT INTO activator (id, zone_id, name, description, gpio_pin) VALUES (1, 1, 'elettrovalvola zona giorno', '', 11);


GRANT ALL PRIVILEGES ON warmme.* TO 'warmme'@'%';