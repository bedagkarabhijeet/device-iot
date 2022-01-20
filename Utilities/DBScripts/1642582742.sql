
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS sensor;
DROP TABLE IF EXISTS device_sensor_mapping;
DROP TABLE IF EXISTS sensor_events;

CREATE TABLE IF NOT EXISTS device (
   device_id SERIAL,
   device_hardware_id  uuid  UNIQUE,
   device_name TEXT,
   is_deleted boolean  DEFAULT false,
   PRIMARY KEY (device_id)
);

CREATE TABLE IF NOT EXISTS sensor (
   sensor_id SERIAL,
   sensor_hardware_id  uuid  UNIQUE,
   sensor_name TEXT NOT NULL,
   sensor_type TEXT NOT NULL, /* Can add another table for sensor type */
   is_deleted boolean DEFAULT false,
   PRIMARY KEY (sensor_id)
);

CREATE TABLE IF NOT EXISTS device_sensor_mapping (
   device_id int,
   sensor_id int
);

CREATE TABLE IF NOT EXISTS sensor_events (
   sensor_id int,
   sensor_value int,
   time_stamp bigint NOT NULL
);

/*
CREATING INDEX pn time_stamp column for for search of sensor events
*/
CREATE INDEX ON sensor_events (time_stamp);
