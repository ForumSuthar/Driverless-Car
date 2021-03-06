ó
¡cª[c           @   sÂ   d  d l  Z d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l	 Z	 d  d l
 m Z d  d l m Z d d
 d     YZ e d k r¾ e j d	  e   Z e j   n  d S(   iÿÿÿÿN(   t   Lock(   t   PoseStamped(   t	   LaserScan(   t   GetMapt   FakeURGNodec           B   s,   e  Z d    Z d   Z d   Z d   Z RS(   c         C   sÖ  t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d	 d
   |  _ t  t j d d   |  _ t  t j d d   |  _	 t
 j |  j |  j	 |  j d t
 j |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ t  t j d d   |  _ |  j   } t j |  } t |  j | j j  } t j | | |  j  |  _ t j   |  _ t j    |  _! t j" j#   } |  j! j$ d d | t j% d   |  j! j& d d |  \ } } d  |  j d! | d" |  _' t j( d# t) d$ d% |  _* t j+ d& t,  t j- t j% j. d' |  j  |  j/  |  _0 d  S((   Ns   ~update_rateg      $@s   ~theta_discretizationi  s   ~min_range_metersg{®Gáz?s   ~max_range_metersgffffff@s   ~angle_stepg.ÿÿ_û!y?s
   ~angle_ming
äÿß° Às
   ~angle_maxgÔÿß!½ @t   dtypes   ~car_lengthgëQ¸Õ?s   ~z_shortg¸ëQ¸?s   ~z_maxg{®GázÄ?s   ~z_blackout_maxi2   s   ~z_randg{®Gáz?s   ~z_hitgé?s   ~z_sigmat	   base_linkt   laserg      @iÿÿÿÿg       @i    s   /scant
   queue_sizei   s   /sim_car_pose/poseg      ð?(1   t   floatt   rospyt	   get_paramt   UPDATE_RATEt   THETA_DISCRETIZATIONt   MIN_RANGE_METERSt   MAX_RANGE_METERSt
   ANGLE_STEPt	   ANGLE_MINt	   ANGLE_MAXt   npt   aranget   float32t   ANGLESt
   CAR_LENGTHt   Z_SHORTt   Z_MAXt   Z_BLACKOUT_MAXt   Z_RANDt   Z_HITt   Z_SIGMAt   get_mapt
   range_libct   PyOMapt   intt   infot
   resolutiont
   PyCDDTCastt   range_methodt   tft   TransformBroadcastert   brt   TransformListenert   tlt   Timet   nowt   waitForTransformt   Durationt   lookupTransformt   x_offsett	   PublisherR   t	   laser_pubt   wait_for_messageR   t   Timert   from_sect   timer_cbt   update_timer(   t   selft   map_msgt   occ_mapt   max_range_pxR,   t   positiont   orientation(    (    s   fake_urg_node.pyt   __init__   s8    *"c      
   C   sd  t  j | j d d t  j } |  j |  j |  j } t |  j | | j d  } t |  j | | j d  } | j d | | } d | | | | +d | | | )t  j j |  | d k } | | c t  j j	 d d d |  j
 d |  7<| d k } t  j j d	 |  j d
 |  j d |  | | <| d k }	 t  j j d	 |  j d
 | |	 d |  | |	 <|  j | |  j | j d }
 xÜ |
 d k r_t  j j d	 d d
 | j d d d  } t  j j d	 d d
 |  j d d  } x} | d k r[| | j d k  r[| d k r[|
 d k r[t  j | |  sWt  j | | <| d 7} | d 8} |
 d 8}
 qßPqßWqWd  S(   Ni    R   i   i   t   locg        t   scalet   sizet   lowt   high(   R   t   zerost   shapeR!   R   R   R   t   randomt   shufflet   normalR   t   uniformR   R   R   t   randintR   t   isnant   nan(   R8   t   rangest   indicest   prob_sumt	   hit_countt
   rand_countt   short_countt   hit_indicest   rand_indicest   short_indicest	   max_countt   curt   blackout_count(    (    s   fake_urg_node.pyt   noise_laser_scan3   s2    /,-($:

c         C   s  t  j j   } t   } d | j _ | | j _ |  j | _ |  j	 | _
 |  j | _ |  j | _ |  j | _ g  | _ t j t |  j  d d t j } t   } d | j _ t  j d  | j _ |  j | j j _ d | j j _ d | j j _ d | j j _ d | j j _ d | j j _ d | j j _ |  j  j! d |  } t j" | j j j | j j j t# j$ | j j  f d t j j% d d	  } |  j& j' | |  j |  |  j( |  | j)   | _* |  j+ j, |  |  j- j. | d | d d f t/ j0 j1 d d | d  | d d  d  S(   NR   i   R   t   sim_posei    g        g      ð?t   mapi   i   (   i    i    (   i    i   (   i    i   (2   R
   R+   R,   R   t   headert   frame_idt   stampR   t   angle_incrementR   t	   angle_minR   t	   angle_maxR   t	   range_minR   t	   range_maxt   intensitiesR   RD   t   lenR   R   R   R0   t   poseR<   t   xt   yt   zR=   t   wR*   t   transformPoset   arrayt   utilst   quaternion_to_anglet   reshapeR%   t   calc_range_repeat_anglesRY   t   tolistRM   R2   t   publishR(   t   sendTransformR&   t   transformationst   quaternion_from_euler(   R8   t   eventR,   t   lsRM   t   ps1t
   laser_poset
   range_pose(    (    s   fake_urg_node.pyR6   S   s>    		%	0c         C   s;   t  j d d  } t  j |  t  j | t    j } | S(   Ns   ~static_mapt
   static_map(   R
   R   t   wait_for_servicet   ServiceProxyR   R[   (   R8   t   map_service_nameR9   (    (    s   fake_urg_node.pyR   y   s    (   t   __name__t
   __module__R>   RY   R6   R   (    (    (    s   fake_urg_node.pyR      s   	%	 	&t   __main__t   fake_urg_node(    (   t   numpyR   R
   R   R&   t	   threadingR    t   geometry_msgs.msgR   Rm   t   sensor_msgs.msgR   t   nav_msgs.srvR   R   R   t	   init_nodet   furgnt   spin(    (    (    s   fake_urg_node.pyt   <module>   s   s	