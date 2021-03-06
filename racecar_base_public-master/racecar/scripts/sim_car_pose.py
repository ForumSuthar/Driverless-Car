ó
¡cª[c           @   sØ   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z m Z d  d l	 m
 Z
 d  d l m Z d  d l m Z d  d l m Z d d d     YZ e d	 k rÔ e  j d
  e   Z e  j   n  d S(   iÿÿÿÿN(   t   PoseWithCovarianceStampedt   PoseStamped(   t   VescStateStamped(   t   Float64(   t   Lock(   t   GetMapt
   SimCarPosec           B   s>   e  Z d    Z d   Z d   Z d   Z d   Z d   Z RS(   c         C   s  t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d	 d
   |  _ t  t j d d   |  _ t  t j d d   |  _	 t  t j d d   |  _
 t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ |  j   \ |  _ |  _ t |  _ d  |  _ d  |  _ t   |  _ d  |  _ t   |  _  d  |  _! t   |  _" d  |  _# t$ j%   |  _# t j& d t' d d |  _( t j) d  t* |  j+ d d |  _, t j) d! t- |  j. d d |  _/ t j) d" t0 |  j1 d d |  _2 t j3 t j4 j5 d# |  j  |  j6  |  _7 d  S($   Ns   /vesc/speed_to_erpm_offsetg        s   /vesc/speed_to_erpm_gaing     ²@s$   /vesc/steering_angle_to_servo_offsetg~¹k	ùà?s"   /vesc/steering_angle_to_servo_gaingÑ"Ûù~jó¿s   ~update_rateg      4@s   ~speed_offsets   ~speed_noiseg-Cëâ6?s   ~steering_angle_offsets   ~steering_angle_noisegíµ ÷Æ°>s   ~forward_offsets   ~forward_fix_noisegH¯¼ò×z>s   ~forward_scale_noisegü©ñÒMbP?s   ~side_offsets   ~side_fix_noises   ~side_scale_noises   ~theta_offsets   ~theta_fix_noises   ~car_lengthgëQ¸Õ?s   /sim_car_pose/poset
   queue_sizei   s   /initialposes   /vesc/sensors/cores$   /vesc/sensors/servo_position_commandg      ð?(8   t   floatt   rospyt	   get_paramt   SPEED_TO_ERPM_OFFSETt   SPEED_TO_ERPM_GAINt   STEERING_TO_SERVO_OFFSETt   STEERING_TO_SERVO_GAINt   UPDATE_RATEt   SPEED_OFFSETt   SPEED_NOISEt   STEERING_ANGLE_OFFSETt   STEERING_ANGLE_NOISEt   FORWARD_OFFSETt   FORWARD_FIX_NOISEt   FORWARD_SCALE_NOISEt   SIDE_OFFSETt   SIDE_FIX_NOISEt   SIDE_SCALE_NOISEt   THETA_OFFSETt   THETA_FIX_NOISEt
   CAR_LENGTHt   get_mapt   permissible_regiont   map_infot   Falset   can_stept   Nonet
   last_stampt
   last_speedR   t   last_speed_lockt   last_steering_anglet   last_steering_angle_lockt   cur_poset   cur_pose_lockt   brt   tft   TransformBroadcastert	   PublisherR   t   cur_pose_pubt
   SubscriberR    t   init_pose_cbt   init_pose_subR   t   speed_cbt	   speed_subR   t   servo_cbt	   servo_subt   Timert   Durationt   from_sect   timer_cbt   update_timer(   t   self(    (    s   sim_car_pose.pyt   __init__   sD    						!!!c         C   s  t  j | j j j j | j j j j t j | j j j  g  } t j	 | |  j
  } |  j t | d d  t | d d  f d k r|  j j   t  j | d | d | d g  |  _ |  j j   |  j r|  j d  k	 r|  j d  k	 rt |  _ qn  d  S(   Ni   g      à?i    i   (   t   npt   arrayt   poset   positiont   xt   yt   utilst   quaternion_to_anglet   orientationt   world_to_mapR   R   t   intR)   t   acquireR(   t   releaseR!   R$   R"   R&   t   True(   R;   t   msgt   rx_poset   map_rx_pose(    (    s   sim_car_pose.pyR0   >   s    5'(c         C   so   |  j  j   | j j |  j |  j |  _ |  j  j   |  j rk |  j	 d  k	 rk |  j d  k	 rk t |  _ n  d  S(   N(   R%   RH   t   statet   speedR   R   R$   RI   R!   R(   R"   R&   RJ   (   R;   RK   (    (    s   sim_car_pose.pyR2   K   s
    (c         C   sl   |  j  j   | j |  j |  j |  _ |  j  j   |  j rh |  j d  k	 rh |  j
 d  k	 rh t |  _ n  d  S(   N(   R'   RH   t   dataR   R   R&   RI   R!   R(   R"   R$   RJ   (   R;   RK   (    (    s   sim_car_pose.pyR4   S   s
    (c         C   sÜ  |  j  s d  St j j   } |  j d  k r7 | |  _ n  | |  j j   } |  j j   |  j	 t
 j j d |  j |  j	 d |  j d d  } |  j j   |  j j   |  j t
 j j d |  j |  j d |  j d d  } |  j j   |  j j   t
 j |  j  } t
 j |  d k  ra| t
 j |  j d  | } | t
 j |  j d  | } d }	 nº t
 j d t
 j |   }
 t
 j d |
  } | |  j | | }	 |  j | t
 j |  j d |	  t
 j |  j d  } |  j | d	 t
 j |  j d |	  t
 j |  j d  } | d c | t
 j j d |  j d |  j d d  t
 j j d d
 d t
 j |  |  j d d  7<| d c | t
 j j d |  j  d |  j! d d  t
 j j d d
 d t
 j |  |  j" d d  7<| d c |	 t
 j j d |  j# d |  j$ d d  7<x2 | d d t
 j% k rL| d c d t
 j% 8<qWx2 | d d t
 j% k  r| d c d t
 j% 7<qPWt& j' | |  j(  } |  j) t* | d d  t* | d d  f d k rát
 j |  |  _ n  t+   } d | j, _- | | j, _. |  j d | j/ j0 _1 |  j d | j/ j0 _2 d
 | j/ j0 _3 t& j4 |  j d  | j/ _5 |  j6 j7 |  | |  _ |  j8 j9 | j/ j0 j1 | j/ j0 j2 | j/ j0 j3 f t: j; j< d d |  j d  | d d  |  j j   d  S(   Nt   loct   scalet   sizei   g{®Gáz?i   i    g      à?iÿÿÿÿg        t   mapt   sim_pose(=   R!   R	   t   Timet   nowR#   R"   t   to_secR%   RH   R$   R=   t   randomt   normalR   R   RI   R'   R&   R   R   R)   R>   R(   t   abst   cost   sint   arctant   tanR   R   R   R   R   R   R   R   R   t   piRC   RF   R   R   RG   R   t   headert   frame_idt   stampR?   R@   RA   RB   t   zt   angle_to_quaternionRE   R.   t   publishR*   t   sendTransformR+   t   transformationst   quaternion_from_euler(   R;   t   eventRW   t   dtt   vt   deltat   new_poset   dxt   dyt   dthetat   betat   sin2betat   new_map_poset   ps(    (    s   sim_car_pose.pyR9   Z   s\    	55	9=dd55		0c         C   s   t  j d d  } t  j |  t  j | t    j } | j } t j | j	  j
 | j j | j j f  } t j | d t } d | | d k <| | f S(   Ns   ~static_mapt
   static_mapt   dtypei   i    (   R	   R
   t   wait_for_servicet   ServiceProxyR   RT   t   infoR=   R>   RP   t   reshapet   heightt   widtht
   zeros_liket   bool(   R;   t   map_service_namet   map_msgR   t	   array_255R   (    (    s   sim_car_pose.pyR      s    	-(   t   __name__t
   __module__R<   R0   R2   R4   R9   R   (    (    (    s   sim_car_pose.pyR      s   	.				At   __main__t   sim_car_pose_node(    (   R	   t   numpyR=   R+   t   tf.transformationsRC   t   geometry_msgs.msgR    R   t   vesc_msgs.msgR   t   std_msgs.msgR   t	   threadingR   t   nav_msgs.srvR   R   R   t	   init_nodet   scpt   spin(    (    (    s   sim_car_pose.pyt   <module>   s   	