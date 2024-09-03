System :
    - products
    - account [activation,email]
    - orders , track order
    - conpons
    - payments
    - dashboard
    -----------------------------
    - celery , redis
    - cashing
    - optnization
    - django command
    - translation
    - ajax
    - docker
    - deploy [herocu - aws]
    -----------------------------
    - api
    - docs
--------------------------------------
products :
    - name
    - sku
    - brand          * [name,image]
    - images         *
    - subtitle      
    - description
    - tags           * package
    - price
    - flag [new-sale-festure] dropdown
    - quanitity
    - reviwes        * [user_id,product_id,reat[0:5],feedback,datetime]
    - category       * [name,img]


order :
    -ststus [recieved,processed,shipped,delivered]
    - user
    - id 
    - total items
    - delivery time
    - order time
    - total
    - sub_total

OrderDetails :
    - order_id
    - product_id 
    - price 
    - quantity
    - total

User :
    - address *
    - name
    - email
    - image
    - phone_numper *
------------------------------


     