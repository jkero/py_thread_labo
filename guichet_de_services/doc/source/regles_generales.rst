Règles et approche générales
============================

.. uml::

    @startuml
        skinparam linetype ortho
        entity "Règle" as r01 {
        * r_id : number <<generated>>
        * name : text
          description : text

        }

       entity "Guichet" as e02 {
       * g_id : number <<generated>>
       * type : text

       other_details : text
        }

       r01 ||--o{e02
    @enduml

ps: \|o = zéro ou n