/*==============================================================*/
/* Table: Pacient                                               */
/*==============================================================*/
create table Pacient
(
   kzz                            int                            not null,
   starost                        int,
   spol                           char(1),
   primary key (kzz)
);

/*==============================================================*/
/* Table: diagnoza                                              */
/*==============================================================*/
create table diagnoza
(
   st_obravnave                   int                            not null,
   st_diagnoze                    int                            not null,
   ICD_diagnoza                   varchar(10),
   primary key (st_obravnave, st_diagnoze)
);

/*==============================================================*/
/* Index: diagnoza_v_obravnavi_FK                               */
/*==============================================================*/
create index diagnoza_v_obravnavi_FK on diagnoza
(
   st_obravnave
);

/*==============================================================*/
/* Table: izvid                                                 */
/*==============================================================*/
create table izvid
(
   st_obravnave                   int                            not null,
   ime_preiskave                  varchar(50)                    not null,
   datum_ura                      datetime                       not null,
   vrednost                       float(2),
   primary key (st_obravnave, ime_preiskave, datum_ura)
);

/*==============================================================*/
/* Index: obravnavan_izvid_FK                                   */
/*==============================================================*/
create index obravnavan_izvid_FK on izvid
(
   st_obravnave
);

/*==============================================================*/
/* Index: preiskava_izvid_FK                                    */
/*==============================================================*/
create index preiskava_izvid_FK on izvid
(
   ime_preiskave
);

/*==============================================================*/
/* Table: koda_diagnoza                                         */
/*==============================================================*/
create table koda_diagnoza
(
   who_koda                       varchar(10),
   mkb_koda                       varchar(10),
   id_kode                        int                            not null,
   opis_kode                      varchar(100)
);

/*==============================================================*/
/* Table: obravnava                                             */
/*==============================================================*/
create table obravnava
(
   st_obravnave                   int                            not null,
   kzz                            int                            not null,
   sifra_oddelka                  int                            not null,
   primary key (st_obravnave)
);

/*==============================================================*/
/* Index: je_obravnavan_FK                                      */
/*==============================================================*/
create index je_obravnavan_FK on obravnava
(
   kzz
);

/*==============================================================*/
/* Index: cakalna_vrsta_FK                                      */
/*==============================================================*/
create index cakalna_vrsta_FK on obravnava
(
   sifra_oddelka
);

/*==============================================================*/
/* Table: oddelek                                               */
/*==============================================================*/
create table oddelek
(
   sifra_oddelka                  int                            not null,
   primary key (sifra_oddelka)
);

/*==============================================================*/
/* Table: preiskava                                             */
/*==============================================================*/
create table preiskava
(
   ime_preiskave                  varchar(50)                    not null,
   sifra_preiskave                int,
   enota                          varchar(10),
   min_rez                        float(2),
   max_rez                        float(2),
   min_m                          float(2),
   max_m                          float(2),
   min_z                          float(2),
   max_z                          float(2),
   primary key (ime_preiskave)
);
