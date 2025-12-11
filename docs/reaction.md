# Reaction

test description

<details markdown="1"><summary markdown="1"> **Legend** </summary>

- **Description:**A short description for Comprehension purposes

- **Data Type:** This specifies exactly what kind of information belongs in this field. Most simply, it could be a direct value, such as a number (float) or a piece of text (string). However, the Data Type can also point to another Class in the schema. When this happens, the field is not just a single value; it becomes a structured container. Designating a Class as the Data Type causes the field to contain a complete structured record, defined entirely by its own comprehensive collection of specific fields. Consequently, this allows for the systematic construction of complex data structures via organized, nested information layers within the broader schema architecture.

- **Cardinality:** This controls how many entries a specific data field must have. It defines if a field is required or optional, and whether it can accept a single value versus a list of multiple values.

- **CURIE:** A CURIE (Compact URI) is a short, easy-to-read reference that acts as a useful shortcut for a long, complex web address. Instead of seeing a full URL, you will see a two-part reference like gene:symbol, where the parts are separated by a colon. The first part is the prefix (a short code for the source website), and the second is the local identifier for the specific item. This structure is much easier to read and type, making the schema less cluttered and reducing errors. The full web link (URI) for the CURIE is always available if you click the provided link.

- **Schema Reference:** This link directs you to the complete, technical documentation for this part of the schema. This detailed view is generated automatically by LinkML’s documentation tool and provides all underlying rules, data types, and complex relationships for expert users and developers.

- **Slots:** A Slot represents an individual data field or attribute that belongs to a specific Class (entity type) within the schema. If a Class defines an entity like 'Book', the Slots define the individual pieces of information about that book, such as the 'title', 'author', and 'ISBN'. Essentially, Slots are the essential building blocks that define the characteristics and permissible data for every record in the schema.

- **Enumerations:** Often called an Enum, Enumerations are a predefined, fixed list of permissible values that a Slot can accept. It is used to strictly limit the available choices for a data field to ensure consistency and prevent errors. For example, a 'Status' field might be restricted to the Enumeration list of only 'Active', 'Inactive', or 'Pending'. Any data entered that is not on this fixed list is considered invalid by the schema.

</details>## Slots

<details markdown="1">
<summary><strong>catalyst quantity</strong> (Required, Multivalued)</summary>

**Description:** Quantity of catalyst used

**Data Type:** float

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:catalyst_quantity`](https://w3id.org/nfdi4cat/catcore/catalyst_quantity)

**Schema Reference:** [catalyst_quantity](./elements/catalyst_quantity.md)

**Unit:** g

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_quantity target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactor design type</strong> (Required, Multivalued)</summary>

**Description:** Type of reactor design

**Data Type:** ReactorDesignType

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0007018`](https://w3id.org/nfdi4cat/voc4cat_0007018)

**Schema Reference:** [reactor_design_type](./elements/reactor_design_type.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ReactorDesignType</strong></summary>

**Abstract Class**

**Description:** Type of reactor design used

**Schema Reference:** [ReactorDesignType](./elements/ReactorDesignType.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ReactorDesignType target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

**Possible Subclasses / Enumerations of ReactorDesignType:**

<details markdown="1">
<summary><strong>ElectrochemicalReactor</strong></summary>

**Description:** Electrochemical reactor

**CURIE:** [`voc4cat:0000193`](https://w3id.org/nfdi4cat/voc4cat_0000193)

**Schema Reference:** [ElectrochemicalReactor](./elements/ElectrochemicalReactor.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectrochemicalReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>CSTR</strong></summary>

**Description:** Continuous stirred tank reactor

**CURIE:** [`voc4cat:0007019`](https://w3id.org/nfdi4cat/voc4cat_0007019)

**Schema Reference:** [CSTR](./elements/CSTR.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CSTR target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>PlugFlowReactor</strong></summary>

**Description:** Plug flow reactor model

**CURIE:** [`voc4cat:0007102`](https://w3id.org/nfdi4cat/voc4cat_0007102)

**Schema Reference:** [PlugFlowReactor](./elements/PlugFlowReactor.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlugFlowReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Autoclave</strong></summary>

**Description:** Autoclave reactor

**CURIE:** [`NCIT:C93052`](http://purl.obolibrary.org/obo/NCIT_C93052)

**Schema Reference:** [Autoclave](./elements/Autoclave.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Autoclave target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>SlurryReactor</strong></summary>

**Description:** Slurry reactor

**CURIE:** [`catcore:SlurryReactor`](https://w3id.org/nfdi4cat/catcore/SlurryReactor)

**Schema Reference:** [SlurryReactor](./elements/SlurryReactor.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SlurryReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>Microreactor</strong></summary>

**Description:** Microreactor

**CURIE:** [`voc4cat:0000234`](https://w3id.org/nfdi4cat/voc4cat_0000234)

**Schema Reference:** [Microreactor](./elements/Microreactor.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Microreactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>FixedBedReactor</strong></summary>

**Description:** Fixed bed reactor

**CURIE:** [`catcore:FixedBedReactor`](https://w3id.org/nfdi4cat/catcore/FixedBedReactor)

**Schema Reference:** [FixedBedReactor](./elements/FixedBedReactor.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FixedBedReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<details markdown="1">
<summary><strong>FluidizedBedReactor</strong></summary>

**Description:** Fluidized bed reactor

**CURIE:** [`catcore:FluidizedBedReactor`](https://w3id.org/nfdi4cat/catcore/FluidizedBedReactor)

**Schema Reference:** [FluidizedBedReactor](./elements/FluidizedBedReactor.md)

**Slots**

<details markdown="1">
<summary><strong>gas distributor type</strong> (Optional, Multivalued)</summary>

**Description:** Type of gas distributor

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gas_distributor_type`](https://w3id.org/nfdi4cat/catcore/gas_distributor_type)

**Schema Reference:** [gas_distributor_type](./elements/gas_distributor_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gas_distributor_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bed expansion height</strong> (Optional, Multivalued)</summary>

**Description:** Bed expansion height

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:bed_expansion_height`](https://w3id.org/nfdi4cat/catcore/bed_expansion_height)

**Schema Reference:** [bed_expansion_height](./elements/bed_expansion_height.md)

**Unit:** cm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bed_expansion_height target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bubble size distribution</strong> (Optional)</summary>

**Description:** No description available

**Data Type:** string

**Cardinality:**  Optional

**Schema Reference:** [bubble_size_distribution](./elements/bubble_size_distribution.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bubble_size_distribution target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FluidizedBedReactor target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_design_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactant</strong> (Required, Multivalued)</summary>

**Description:** Reactant used in the reaction

**Data Type:** string

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000101`](https://w3id.org/nfdi4cat/voc4cat_0000101)

**Schema Reference:** [reactant](./elements/reactant.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactant target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>operation parameters</strong> (Required, Multivalued)</summary>

**Description:** Operation parameters for the reaction

**Data Type:** OperationParameters

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000142`](https://w3id.org/nfdi4cat/voc4cat_0000142)

**Schema Reference:** [operation_parameters](./elements/operation_parameters.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>OperationParameters</strong></summary>

**Description:** Operation parameters for the reaction

**Schema Reference:** [OperationParameters](./elements/OperationParameters.md)

**Slots**

<details markdown="1">
<summary><strong>reactor temperature range</strong> (Optional, Multivalued)</summary>

**Description:** Temperature range in reactor

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007032`](https://w3id.org/nfdi4cat/voc4cat_0007032)

**Schema Reference:** [reactor_temperature_range](./elements/reactor_temperature_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_temperature_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>experiment pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure during experiment

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000118`](https://w3id.org/nfdi4cat/voc4cat_0000118)

**Schema Reference:** [experiment_pressure](./elements/experiment_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_pressure target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>feed composition range</strong> (Optional, Multivalued)</summary>

**Description:** Range of feed composition

**Data Type:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:feed_composition_range`](https://w3id.org/nfdi4cat/catcore/feed_composition_range)

**Schema Reference:** [feed_composition_range](./elements/feed_composition_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20feed_composition_range target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>experiment duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the experiment

**Data Type:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002455`](http://purl.allotrope.org/ontologies/result#AFR_0002455)

**Schema Reference:** [experiment_duration](./elements/experiment_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_duration target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20OperationParameters target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_parameters target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>product identification method</strong> (Required, Multivalued)</summary>

**Description:** Method used for product identification

**Data Type:** ProductIdentificationMethod

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000129`](https://w3id.org/nfdi4cat/voc4cat_0000129)

**Schema Reference:** [product_identification_method](./elements/product_identification_method.md)

**Data Type Class Details:**

<details markdown="1">
<summary><strong>ProductIdentificationMethod</strong></summary>

**Abstract Class**

**Description:** Method used for product identification

**Schema Reference:** [ProductIdentificationMethod](./elements/ProductIdentificationMethod.md)

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ProductIdentificationMethod target="_blank" class="md-button md-button--primary">
        💡 Submit Term Feedback
      </a>
    </p></details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20product_identification_method target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst type</strong> (Recommended, Multivalued)</summary>

**Description:** Type of catalyst

**Data Type:** string

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`voc4cat:0007014`](https://w3id.org/nfdi4cat/voc4cat_0007014)

**Schema Reference:** [catalyst_type](./elements/catalyst_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_type target="_blank" class="md-button md-button--primary">
    💡 Submit Term Feedback
  </a>
</p></details>

<iframe
    src="assets/chart_reaction.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>